import os
import json
import pandas as pd

from google import genai
from google.genai import types

from sqlalchemy import create_engine,text
from dotenv import load_dotenv
from datetime import datetime

# ==========================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please add your Gemini API key to the .env file."
    )


# ==========================================================
# 2. INITIALIZE GEMINI CLIENT
# ==========================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ==========================================================
# 3. LOAD CUSTOMER FEEDBACK CSV
# ==========================================================

df = pd.read_csv("customer_feedback.csv")

print("\n========================================")
print("Original CSV Data")
print("========================================")

print(df.head())

print("\nTotal CSV rows:", len(df))


# ==========================================================
# 4. DATA CLEANING
# ==========================================================

# Remove duplicate feedbackID

df = df.drop_duplicates(
    subset=["FeedbackID"]
)

# Handle missing feedback
df["Feedback"] = (
    df["Feedback"]
    .fillna("")
    .astype(str)
)

# Convert date 

df["FeedbackDate"] = pd.to_datetime(
    df["FeedbackDate"],
    errors="coerce"
)

# Convert rating 

df["Rating"] = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

# Remove rows where important columns are missing

df = df.dropna(
    subset=[
        "FeedbackID",
        "CustomerID",
        "FeedbackDate",
        "Rating"
    ]
)

# Convert FeedbackID to integer

df["FeedbackID"]=(df["FeedbackID"].astype(int))


## Convert rating integer

df["Rating"]=(df["Rating"].astype(int))

print("\n========================================")
print("Cleaned Data")
print("========================================")


print(df.head())

print("\ncleaned rows:",len(df))



# ==========================================================
# 5. GEMINI CUSTOMER FEEDBACK ANALYSIS
# ==========================================================

def analyze_feedback(feedback):

    prompt = f"""
You are a professional Customer Feedback Analytics AI.

Analyze the following customer feedback:

Customer Feedback:
{feedback}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "sentiment": "Positive",
    "category": "Product",
    "emotion": "Satisfied",
    "priority": "Low",
    "summary": "Short summary of the feedback",
    "action": "Recommended business action"
}}

Rules:

sentiment:
Positive, Neutral, or Negative

category:
Product, Delivery, Support, Price, or Other

emotion:
Happy, Angry, Disappointed, Neutral, or Satisfied

priority:
Low, Medium, or High

summary:
Give a short business-friendly summary.

action:
Give one practical recommendation for the business.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json"
            )
        )

    
        result_json = json.loads(response.text)

        return result_json

    except Exception as e:

        print("\nGemini Error:", e)

        # Return default values if API fails
        return {
            "sentiment": "Unknown",
            "category": "Other",
            "emotion": "Neutral",
            "priority": "Low",
            "summary": "AI analysis failed",
            "action": "Review feedback manually"
        }


# ==========================================================
# 6. ANALYZE EVERY CUSTOMER FEEDBACK
# ==========================================================

analysis_results = []

for index,feedback in enumerate(
    df["Feedback"], 
    start=1
    ):

    print(f"\nAnalyzing Feedback{index}" 
          f"of {len(df)}"
          
    )
    
    print(feedback)

    result = analyze_feedback(
        feedback
    )

    analysis_results.append(
        result
    )


# ==========================================================
# 7. CONVERT AI RESULTS INTO DATAFRAME
# ==========================================================

analysis_df = pd.DataFrame(
    analysis_results
)


# ADD AI results to original datframe

df = pd.concat(
    [
        df.reset_index(drop=True),
        analysis_df.reset_index(drop=True)
    ],
    axis=1
)

# ==========================================================
# 8. BUSINESS METRICS
# ==========================================================

# Negative feedback flag

df["NegativeFlag"] = (
    df["sentiment"] == "Negative"
).astype(int)


# High priority flag

df["HighPriorityFlag"] = (
    df["priority"] == "High"
).astype(int)


# Month column 

df["Month"] = (
    df["FeedbackDate"]
    .dt.to_period("M")
    .astype(str)
)

# ==========================================================

9. #Rename AI Columns

# ==========================================================

df.rename(
    columns={
        
        "sentiment": "Sentiment",
        "category": "Category",
        "emotion": "Emotion",
        "priority": "Priority",
        "summary": "Summary",
        "action": "Action"
        
    },
    
    inplace=True
    
)



# ==========================================================
# 10. DISPLAY FINAL Python DATA
# ==========================================================

print("\n========================================")
print("FINAL PYTHON DATA")
print("========================================")

print(
    df[
        [
            "FeedbackID",
            "CustomerID",
            "FeedbackDate",
            "Rating",
            "Feedback",
            "Sentiment",
            "Category",
            "Emotion",
            "Priority",
            "Summary",
            "Action",
            "NegativeFlag",
            "HighPriorityFlag",
            "Month"
        ]
    ]
)


# ==========================================================
# 11. SAVE Final CSV
# ==========================================================

current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

output_file = (
    "customer_feedback_ai_analysis_" + current_datetime + ".CSV"
)

df.to_csv(
    output_file,
    index=False
)

print(
    f"\nCSV successfully created:" 
    f"{output_file}"
)


# ==========================================================
# 12. SQL SERVER CONNECTION
# ==========================================================

server = r"DESKTOP-2V74QG8\SQLEXPRESS"
database = "CustomerAnalytics"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=Yes"
 
)

engine = create_engine(connection_string)


# ==========================================================

# 13. TEST SQL SERVER CONNECTION

# ==========================================================

try:
    
    with engine.connect() as connection:
        connection.execute(
            text("SELECT 1")
        )
        
        print( "\n========================================" )
        
        print("SQL SERVER CONNECTED SUCCESSFULLY")
        
        print( "========================================" )

except Exception as e:
    
    print("\nSQL SERVER CONNECTION ERROR:")
    
    print(e)
    
    raise SystemExit



# ==========================================================
# 14. INSERT PYTHON DATA INTO SQL SERVER
# ==========================================================

try:

    df.to_sql(
        name="CustomerFeedbackAI",
        con=engine,
        if_exists="append",
        index=False,
        chunksize=100
        
    )
    
    print( "\n========================================" )

    print("PYTHON DATA INSERTED INTO SQL SERVER")
    
    print( "========================================" )

except Exception as e:
    
    print( "\n========================================" )

    print("SQL SERVER INSERT ERROR")
        
    print( "========================================" )

    print(e)
    
    raise SystemExit
    
# ==========================================================

# 15. READ DATA BACK FROM SQL SERVER

# ==========================================================

try:
    
    verification_query="""
    
    SELECT *
    FROM CustomerFeedbackAI
    ORDER BY AnalysisDateTime DESC
    
    """
    
    sql_data = pd.read_sql(verification_query, engine)

    print( "\n========================================" )

    print(sql_data)

    print("\nTotal rows in SQL Server:", len(sql_data))

except Exception as e:
    
    print("\nSQL SERVER VERIFICATION ERROR:")
  
    print(e)
  
  
  # ==========================================================      
  
  # 16. FINAL MESSAGE
  
  # ==========================================================
   
    print( "\n========================================" )
  
    print("CUSTOMER FEEDBACK AI PIPELINE COMPLETED")
    
    print( "========================================" )
  
  
    print("""

    CSV
     ↓
    Python + Pandas
     ↓
    Data Cleaning
     ↓
    Gemini AI
     ↓
    Sentiment
    Category
    Emotion
    Priority
    Summary
    Action
     ↓
    Final Python DataFrame
     ↓
    SQL Server
     ↓
    CustomerFeedbackAI
     ↓
    Power BI
     ↓
    AI Customer Feedback Dashboard

    """)


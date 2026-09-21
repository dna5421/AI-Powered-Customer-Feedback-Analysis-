## 🎯 AI-Powered Customer Feedback Analysis 

## 📝 Project Overview

  This project analyzes customer feedback using Python and a generative AI model to classify each review by sentiment, category, emotion, priority, summary, and recommended action. The output is saved as    a CSV and pushed into SQL Server for reporting, with a Power BI dashboard visualization as the final business-facing layer.

## ✨ Problem Statement

  Businesses often receive large volumes of customer feedback across product quality, delivery, support, pricing, and other categories. Manually reviewing each comment is slow, inconsistent, and often       misses urgent issues. This project solves that by automatically labeling comments, highlighting dissatisfied customers and high-priority issues, and creating a data pipeline for business monitoring and    action.


## 📊 Dataset

   ✅ The project uses a small customer feedback dataset in the repository:
   
   ✅ File: customer_feedback.csv
    • Columns:
    • FeedbackID
    • CustomerID
    • FeedbackDate
    • Rating
    • Feedback

   ✅ The sample data includes customer comments with ratings from 1 to 5, covering:
    • Product issues
    • Delivery delays and damage
    • Support responsiveness
    • Pricing satisfaction
   
   ✅ The repo also includes an AI-processed output file:
    • customer_feedback_ai_analysis_2026-09-20_13-11-49.CSV


## ⚒️ Tools and Technologies

 • Python
 • Pandas
 • Google Gemini AI API
 • Python dotenv
 • SQLAlchemy
 • pyodbc / ODBC Driver 17 for SQL Server
 • Microsoft SQL Server
 • Power BI (dashboard workflow mentioned in script)
 • CSV and Excel-style reporting output

## Ⓜ️ METHODS

   1 Load and clean the feedback dataset
    • Remove duplicate FeedbackID values
    • Fill missing comments
    • Convert dates and ratings to proper data types
    • Drop incomplete records

   2 Send each review to Gemini for analysis

   ✅ Prompt asks the AI to return structured JSON with:
    • Sentiment
    • Category
    • Emotion
    • Priority
    • Summary
    • Action

   3 Merge AI analysis results back into the original dataset

   4 Add derived business flags
   • NegativeFlag
   • HighPriorityFlag
   • Month
   
   5 Save the processed file as a CSV

   6 Insert the data into SQL Server

   7 Visualize results in Power BI dashboard


## 📊 Key Insights

   ✅ From the sample dataset:
    • Positive feedback: 4 records
    • Negative feedback: 3 records
    • Neutral feedback: 1 record
    • High-priority complaints: 3 records

   ✅ Main issue areas:
    • Product quality and app stability
    • Delivery problems (damage / late delivery)
    • Support response issues
    
   ✅ Notable examples:
    • Damaged product and poor delivery experience
    • Unanswered complaint
    • App crashes with unhelpful support
    • Strong praise for product quality and support service


## 🧑‍💼 Model/output

   ✅ The AI model used in the script is:
    • Google Gemini (gemini-3.5-flash-lite)
    
   The model returns JSON in this exact structure: { "sentiment": "Positive", "category": "Product", "emotion": "Satisfied", "priority": "Low", "summary": "Short summary of the feedback", "action":           "Recommended business action" }


   ✅ Example output from the repository:

   ✅ Feedback 2:
    • Sentiment: Negative
    • Category: Delivery
    • Emotion: Disappointed
    • Priority: High
    • Summary: Customer received a damaged product and is unhappy with the condition.
    • Action: Initiate a replacement or refund and improve packaging

## 🚀 How To Run This Project

 1 Clone the repository

 2 Create a .env file in the project root

 3 Add your Gemini API key: GEMINI_API_KEY=your_api_key_here

 4 Install Python dependencies:
 
 pip install pandas python-dotenv google-genai sqlalchemy pyodbc

 5 Ensure SQL Server is installed and accessible
  • The script currently targets:
  • Server: DESKTOP-2V74QG8\SQLEXPRESS
  • Database: CustomerAnalytics
  • Update these values to your local environment if needed.

 6 Place the dataset in the same folder:

  customer_feedback.csv

 7 Run:

  python feedback_analysis_gemini.py


 8 The script will:
  • clean the data
  • analyze feedback with Gemini
  • create a processed CSV
  • insert records into SQL Server
  • print a completion summary


 ## 🎯 Results

 ✅ The project successfully demonstrates an end-to-end AI feedback analysis pipeline. It can:

  • classify sentiment
  • identify problem categories
  • flag urgent complaints
  • generate business-friendly summaries
  • save output for analytics and reporting


 ✅ In the sample dataset:

  • Most reviews are positive or neutral, but serious issues exist in delivery and support
  • High-priority negative feedback is actionable and should be escalated quickly
  • Product and support quality are major drivers of both praise and dissatisfaction

## ✨ CONCLUSION

 This project is a practical example of how AI can transform raw customer feedback into quantifiable business intelligence. It bridges customer experience data and operational action by converting free-    text reviews into structured insights for product, support, and logistics teams.


## 🏢 Future Work

 • Use a larger real-world dataset
 • Add multilingual feedback analysis
 • Automate dashboard refreshes
 • Integrate comments from e-commerce, CRM, or social media
 • Add alerting for critical negative reviews
 • Compare Gemini outputs with traditional sentiment models
 • Build a web app or API for real-time reporting


 ## 📡 Author & Contact

   👤 Author: dna5421
   📧 GitHub Profile: https://github.com/dna5421
   🔗 Repository: github.com/dna5421/AI-Powered-Customer-Feedback-Analysis

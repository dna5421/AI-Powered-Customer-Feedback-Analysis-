<body>
<div class="container">

<h1>🎯 AI-Powered Customer Feedback Analysis</h1>

<h2>📝 Project Overview</h2>
<p>This project analyzes customer feedback using<strong>Python</strong> and a <strong>generative AI model</strong>to classify each review by sentiment, category, emotion, priority,summary, and recommended action.</p>

<p>The processed output is saved as a CSV file and inserted into<strong>Microsoft SQL Server</strong> for reporting and analytics.<strong>Power BI</strong> is then used as the final business-facing visualization layer.</p>

<div class="highlight">
    <strong>End-to-End Pipeline:</strong>
    Customer Feedback → Python Cleaning → Gemini AI Analysis →
    Structured Data → SQL Server → Power BI Dashboard
</div>

<h2>📝 Problem Statement</h2>
<p>Businesses often receive large volumes of customer feedback acrossproduct quality, delivery, support, pricing, and other categories.Manually reviewing each comment is slow, inconsistent, and can miss
    urgent issues.</p>

<p>This project automates the analysis process by labeling comments,identifying dissatisfied customers, highlighting high-priority issues,and creating a structured data pipeline for business monitoring and
    decision-making.</p>

<h2>📊 Dataset</h2>

<div class="success">
    <strong>Dataset:</strong> customer_feedback.csv
</div>

<h3>Dataset Columns</h3>

<ul>
    <li>FeedbackID</li>
    <li>CustomerID</li>
    <li>FeedbackDate</li>
    <li>Rating</li>
    <li>Feedback</li>
</ul>

<h3>Feedback Coverage</h3>

<ul>
    <li>Product issues</li>
    <li>Delivery delays and damaged products</li>
    <li>Customer support responsiveness</li>
    <li>Pricing satisfaction</li>
</ul>

<h3>AI-Processed Output</h3>

<p>The repository also contains the processed output:</p>

<code>customer_feedback_ai_analysis_2026-09-20_13-11-49.csv</code>

<h2>⚒️ Tools and Technologies</h2>

<div class="card-container">
    <div class="card"><strong>Programming:</strong>Python, Pandas</div>
    <div class="card"><strong>Generative AI:</strong>Google Gemini AI API</div>
    <div class="card"><strong>Database:</strong>Microsoft SQL Server</div>
    <div class="card"><strong>Database Connectivity:</strong>SQLAlchemy, pyodbc, ODBC Driver 17</div>
    <div class="card"><strong>Visualization:</strong>Microsoft Power BI</div>
    <div class="card"><strong>Data Formats:</strong>CSV and Excel-style reporting</div>
    <div class="card"><strong>Configuration:</strong>Python dotenv</div>

</div>


<h2>Ⓜ️ Methodology</h2>

<ol>
    <li><strong>Load and Clean the Feedback Dataset</strong>
        <ul>
            <li>Remove duplicate FeedbackID values</li>
            <li>Handle missing feedback comments</li>
            <li>Convert dates into proper datetime format</li>
            <li>Convert ratings into numeric values</li>
            <li>Remove incomplete records</li>
        </ul>
    </li>
    <li> <strong>Send Each Review to Gemini AI</strong>
        <p>Each customer review is submitted to Gemini using a structuredprompt that requests JSON output.</p>
    </li>
    <li>
        <strong>AI Classification</strong>
        <ul>
            <li>Sentiment</li>
            <li>Category</li>
            <li>Emotion</li>
            <li>Priority</li>
            <li>Summary</li>
            <li>Recommended Action</li>
        </ul>
    </li>
    <li>
        <strong>Merge AI Results</strong>
        <p>The AI-generated analysis is merged back into the originalcustomer feedback dataset.</p>
    </li>
    <li>
        <strong>Create Business Flags</strong>
        <ul>
            <li>NegativeFlag</li>
            <li>HighPriorityFlag</li>
            <li>Month</li>
        </ul>
    </li>
    <li>
        <strong>Export Processed Data</strong>
        <p>The final analyzed dataset is saved as a CSV file.</p>
    </li>
    <li>
        <strong>Load Data into SQL Server</strong>
        <p>Processed feedback records are inserted into SQL Server for analytics and reporting.</p>
    </li>
    <li>
        <strong>Power BI Dashboard</strong>
        <p>Power BI connects to the structured data and provides interactive business dashboards.</p>
    </li>

</ol>


<h2>🤖 AI Model & Output</h2>

<p>The project uses:</p>

<div class="highlight"><strong>Google Gemini — gemini-3.5-flash-lite</strong></div>

<p>The model is instructed to return structured JSON in the following format:</p>

<pre>{
    "sentiment": "Positive",
    "category": "Product",
    "emotion": "Satisfied",
    "priority": "Low",
    "summary": "Short summary of the feedback",
    "action": "Recommended business action"
}</pre>


<h2>📌 Example AI Output</h2>

<div class="warning">
    <h3>Feedback 2</h3>
    <table>
        <tr>
            <th>Field</th>
            <th>AI Output</th>
        </tr>
        <tr>
            <td>Sentiment</td>
            <td>Negative</td>
        </tr>
        <tr>
            <td>Category</td>
            <td>Delivery</td>
        </tr>
        <tr>
            <td>Emotion</td>
            <td>Disappointed</td>
        </tr>
        <tr>
            <td>Priority</td>
            <td>High</td>
        </tr>
        <tr>
            <td>Summary</td>
            <td>
                Customer received a damaged product and is unhappy
                with the condition.
            </td>
        </tr>
        <tr>
            <td>Action</td>
            <td>
                Initiate a replacement or refund and improve packaging.
            </td>
        </tr>
    </table>

</div>

<h2>📊 Key Insights</h2>

<div class="card-container">
    <div class="card"><strong>Positive Feedback</strong>4 records</div>
    <div class="card"><strong>Negative Feedback</strong>3 records</div>
    <div class="card"><strong>Neutral Feedback</strong>1 record</div>
    <div class="card"><strong>High-Priority Complaints</strong>3 records</div>
</div>

<h3>Main Issue Areas</h3>

<ul>
    <li>Product quality and application stability</li>
    <li>Delivery delays and damaged products</li>
    <li>Customer support response issues</li>
</ul>

<h3>Notable Feedback Examples</h3>

<ul>
    <li>Damaged product and poor delivery experience</li>
    <li>Unanswered customer complaint</li>
    <li>Application crashes combined with unhelpful support</li>
    <li>Strong praise for product quality and support service</li>
</ul>

<h2>🚀 How to Run This Project</h2>

<h3>1. Clone the Repository</h3>

<p>Clone or download the project repository to your local machine.</p>

<h3>2. Configure Gemini API</h3>

<p>Create a <code>.env</code> file in the project root:</p>

<pre>GEMINI_API_KEY=your_api_key_here</pre>

<h3>3. Install Dependencies</h3>

<pre>pip install pandas python-dotenv google-genai sqlalchemy pyodbc</pre>

<h3>4. Configure SQL Server</h3>

<p>The current script targets the following local SQL Server environment:</p>

<pre>Server: DESKTOP-2V74QG8\SQLEXPRESS
Database: CustomerAnalytics</pre>

<p>Update these values according to your local SQL Server configuration.</p>

<h3>5. Add Dataset</h3>

<p>Place the following file in the project folder:</p>

<pre>customer_feedback.csv</pre>

<h3>6. Run the Python Script</h3>

<pre>python feedback_analysis_gemini.py</pre>

<h3>7. Pipeline Execution</h3>

<p>The script will automatically:</p>

<ul>
    <li>Clean the customer feedback data</li>
    <li>Analyze feedback using Gemini AI</li>
    <li>Create the processed CSV file</li>
    <li>Insert analyzed records into SQL Server</li>
    <li>Print a completion summary</li>
</ul>

<h2>🎯 Results</h2>

<div class="success">
    <p>The project demonstrates an end-to-end AI-powered customer feedbackanalysis pipeline that transforms unstructured customer commentsinto structured and actionable business data.</p>

</div>

<ul>
    <li>Automatically classifies customer sentiment</li>
    <li>Identifies feedback categories</li>
    <li>Detects emotions and priority levels</li>
    <li>Flags urgent negative complaints</li>
    <li>Generates business-friendly summaries</li>
    <li>Recommends potential business actions</li>
    <li>Stores processed data for analytics</li>
    <li>Supports Power BI reporting and visualization</li>
</ul>

<h3>Sample Dataset Findings</h3>

<ul>
    <li>Most reviews are positive or neutral, but serious issues exist within delivery and support.</li>
    <li>High-priority negative feedback provides actionable signalsfor customer service and operations teams.</li>
    <li>Product and support quality are important drivers of bothpositive and negative customer experiences.</li>
</ul>

<h2>✨ Conclusion</h2>

<p>This project demonstrates how generative AI can transform rawcustomer feedback into structured business intelligence.</p>

<p>By combining <strong>Python, Gemini AI, SQL Server, and Power BI</strong>,the pipeline converts free-text customer reviews into measurableinsights that can support product, customer support, and logistics teams.</p>

<h2>🏢 Future Work</h2>

<ul>
    <li>Use a larger real-world customer feedback dataset</li>
    <li>Add multilingual feedback analysis</li>
    <li>Automate Power BI dashboard refreshes</li>
    <li>Integrate e-commerce, CRM, and social media feedback</li>
    <li>Add alerts for critical negative reviews</li>
    <li>Compare Gemini results with traditional sentiment models</li>
    <li>Build a web application or REST API for real-time analysis</li>
</ul>

<h2>📡 Author & Contact</h2>

<div class="highlight">
    <p><strong>Author:</strong> dna5421</p>
    <p><strong>GitHub Profile:</strong><a href="https://github.com/dna5421" target="_blank">github.com/dna5421</a></p>
    <p><strong>Repository:</strong><a href="https://github.com/dna5421/AI-Powered-Customer-Feedback-Analysis-" target="_blank">AI-Powered-Customer-Feedback-Analysis</a></p>

</div>

<div class="footer">
    <p>AI-Powered Customer Feedback Analysis |Python • Gemini AI • SQL Server • Power BI</p>
</div>

</div>

</body>
</html>

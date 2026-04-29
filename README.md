AI Study Planner (Streamlit + Gemini AI)
An AI-powered Study Planner web application built using Streamlit and Google Gemini via LangChain. The application generates personalized study schedules based on user input such as subject, daily study hours, and number of days.
It helps learners structure their study routine with realistic daily plans, revision sessions, and practice tasks.

Features
AI-generated personalized study plans
Dynamic scheduling based on available time and duration
Structured breakdown of topics into daily tasks
Includes revision and practice planning
Simple and interactive Streamlit interface
Powered by Google Gemini (via LangChain)
Tech Stack
Python
Streamlit
LangChain
Google Generative AI (Gemini 2.0 Flash Lite)
Project Structure
app.py
Installation
1. Clone the repository
git clone https://github.com/your-username/ai-study-planner.git
cd ai-study-planner
2. Install dependencies
pip install streamlit langchain langchain-google-genai
3. Add API Key

In app.py, set your Google API key:

GOOGLE_API_KEY = "your_api_key_here"
Running the Application
streamlit run app.py

Then open the local server URL provided in the terminal (usually http://localhost:8501
).

How It Works
User enters subject, number of study hours per day, and number of days.
Input is passed into a LangChain prompt template.
Gemini AI generates a structured study plan.
The plan is displayed in the Streamlit UI.
Example Input
Subject: Machine Learning
Hours per day: 3
Days: 7
Output

A structured 7-day study plan including daily topics, revision sessions, and practice tasks.

Future Improvements
Secure API key using environment variables
Export study plan as PDF
Add progress tracking system
Add calendar integration
Improve UI/UX design

Author:
Hamza Raza
Python and AI Developer

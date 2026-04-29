import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# DIRECT API KEY (IN CODE)
# -----------------------------
GOOGLE_API_KEY = ""

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="AI Study Planner", page_icon="📚")

st.title("📚 AI Study Planner")

subject = st.text_input("What do you want to study?")
hours_per_day = st.number_input("Hours per day", 1, 16, 3)
days = st.number_input("Number of days", 1, 365, 7)

generate = st.button("Generate Plan")

# -----------------------------
# LLM
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# -----------------------------
# PROMPT (LCEL STYLE)
# -----------------------------
prompt = ChatPromptTemplate.from_template("""
You are an expert study planner.

Create a structured study plan.

Subject: {subject}
Hours per day: {hours}
Days: {days}

Rules:
- Break into daily schedule
- Include revision days
- Include practice tasks
- Keep it realistic
- Use bullet points
""")

chain = prompt | llm

# -----------------------------
# RUN
# -----------------------------
if generate:
    if not subject:
        st.warning("Type a subject first.")
    else:
        with st.spinner("Generating plan... pretending to be productive 🤖"):
            result = chain.invoke({
                "subject": subject,
                "hours": hours_per_day,
                "days": days
            })

        st.subheader("Your Study Plan")
        st.markdown(result.content)
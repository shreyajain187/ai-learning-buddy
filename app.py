import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Learning Buddy")
st.write("Hello! I'm **ByteBuddy**, your AI tutor.")

topic = st.text_input("Enter a topic")

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Evaluate My Answer",
        "Ask Anything"
    ]
)

question = ""
answer = ""

if activity == "Evaluate My Answer":
    question = st.text_area("Question")
    answer = st.text_area("Your Answer")

if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")
        st.stop()

    if activity == "Explain Concept":
        prompt = f"""
Explain {topic} in simple language.

Use headings.

Give important points.

End with a summary.
"""

    elif activity == "Real-Life Example":
        prompt = f"""
Give a real-life example of {topic}.

Explain why it relates.
"""

    elif activity == "Generate Quiz":
        prompt = f"""
Generate 5 MCQs on {topic}.

Each question should include:

Question

4 Options

Correct Answer

Short Explanation.
"""

    elif activity == "Evaluate My Answer":
        prompt = f"""
Topic:
{topic}

Question:
{question}

Student Answer:
{answer}

Evaluate the answer.

Explain mistakes.

Give the correct answer.

Encourage the learner.
"""

    else:
        prompt = topic

    with st.spinner("Thinking..."):

        response = model.generate_content(prompt)

        st.markdown(response.text)
import streamlit as st
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    # Perform summarization
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

st.title("Text Summarization Application")

# Input text box
text = st.text_area("Enter the text you want to summarize", height=200)

# Summarize button
if st.button("Summarize"):
    if text:
        summary = summarize_text(text)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

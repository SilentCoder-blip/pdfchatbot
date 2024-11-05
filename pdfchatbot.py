from pdfminer.high_level import extract_text  # Using pdfminer for PDF text extraction
import streamlit as st
from transformers import pipeline

# Load a pre-trained question-answering model from Hugging Face
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = extract_text(pdf_file)  # Use pdfminer to extract text
    return text

# Streamlit UI
st.title("PDF Query Chatbot")
st.write("Upload a PDF and ask questions about its content.")

# Upload PDF file
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# Enter question
question = st.text_input("Enter your question:")

if uploaded_file and question:
    # Extract text from the uploaded PDF
    pdf_text = extract_text_from_pdf(uploaded_file)
    
    # Get answer using the Hugging Face model
    result = qa_pipeline(question=question, context=pdf_text)
    
    # Display the answer
    st.write("Answer:", result['answer'])

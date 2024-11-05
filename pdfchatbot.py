import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
import docx

# Load the summarization model
summarizer = pipeline("summarization")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Streamlit UI
st.title("Document Summarizer")
st.write("Upload a document file (.pdf or .docx) to summarize its content.")

uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx'])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file type!")

    if text:
        st.subheader("Original Text:")
        st.write(text)

        # Summarize the text
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])

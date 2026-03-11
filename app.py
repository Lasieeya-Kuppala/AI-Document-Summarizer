import streamlit as st
from summarizer import summarize_document

st.title("AI Document Summarizer")
st.write("Upload a PDF or Word document to generate a summary and key points.")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.info("Summarizing document... please wait.")
    summary, key_points = summarize_document("temp_file")
    
    st.subheader("Summary")
    st.write(summary)
    
    st.subheader("Key Points")
    for point in key_points:
        if point.strip():
            st.write("-", point)

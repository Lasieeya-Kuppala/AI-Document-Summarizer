# AI Document Summarizer

## Project Overview
An AI-powered tool that automatically summarizes long documents (PDFs, Word files, web pages) into concise summaries and key points using OpenAI GPT-4.  

**Target Users:**
- Students needing quick summaries of study material  
- Business analysts reviewing long reports  
- Researchers handling large amounts of text  

## Features
- Upload PDFs or Word documents  
- Automatic text extraction  
- GPT-4 generates a concise summary and key bullet points  
- Streamlit web interface  

## Tech Stack
- Python  
- OpenAI GPT-4 API  
- LangChain  
- PyPDF2 / python-docx  
- Streamlit  

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/AI-Document-Summarizer.git
cd AI-Document-Summarizer
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

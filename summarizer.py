
---

## **2. `summarizer.py`**
```python
import PyPDF2
import docx
import openai

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_text(file_path):
    """Extract text from PDF or Word document"""
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = " ".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        text = " ".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")
    return text

def summarize_document(file_path):
    """Summarize document using GPT-4"""
    text = extract_text(file_path)
    prompt = f"Summarize this document and provide key bullet points:\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content": prompt}],
        max_tokens=500
    )
    
    summary_text = response.choices[0].message.content
    lines = summary_text.split("\n")
    summary = lines[0]
    key_points = lines[1:]
    
    return summary, key_points

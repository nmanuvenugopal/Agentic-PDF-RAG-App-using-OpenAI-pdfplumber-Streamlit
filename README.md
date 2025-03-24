# Agentic-PDF-RAG-App-using-OpenAI-pdfplumber-Streamlit

## 🧠 Agentic PDF RAG App using OpenAI + pdfplumber

### 🔍 Project Overview

This project is a **Streamlit-based Retrieval-Augmented Generation (RAG) app** that allows users to upload complex PDF files—containing **tables, bullet points, paragraphs, and checkboxes**—and query them using natural language.

Using **`pdfplumber`** for accurate PDF text and table extraction, this app combines **OpenAI embeddings**, **FAISS vector search**, and **LangChain agents** to create a powerful, agentic question-answering system grounded in document context.

---

### 📌 Key Features

- 📄 **PDF Text & Table Extraction with `pdfplumber`**  
  Parses raw text and structured data (tables) from each page of the uploaded PDF.

- 🧩 **Contextual Chunking for LLM Consumption**  
  Extracted content is split into semantic chunks using sliding windows to preserve context.

- 🔍 **FAISS + OpenAI Embeddings**  
  Chunks are embedded using OpenAI's `text-embedding-ada-002` model and stored in a FAISS vector index for efficient similarity-based retrieval.

- 🤖 **LangChain Agent with Tool Use**  
  An agent is initialized with access to the document retriever as a tool. It plans, retrieves relevant content, and responds intelligently.

- 💬 **Streamlit Interface**  
  Users can upload PDFs and ask questions through a friendly, interactive UI.

---

### 🛠 Tech Stack

| Tech            | Description                                     |
|------------------|-------------------------------------------------|
| Streamlit        | Frontend for file upload and interaction        |
| pdfplumber       | PDF extraction of text and structured tables    |
| LangChain        | Agent system and tool chaining logic            |
| OpenAI API       | GPT-3.5 for generation and ADA for embeddings   |
| FAISS            | Fast vector similarity search                   |
| Python           | Core programming language                       |

---

### 🔧 How It Works

1. **Upload PDF**  
   User uploads a PDF via the Streamlit interface.

2. **Text Extraction**  
   The backend uses `pdfplumber` to extract raw text (and tables if needed) from all pages.

3. **Chunking**  
   The extracted text is divided into context-preserving chunks using a sliding window strategy (e.g., 500-word chunks with 100-word overlap).

4. **Embedding & Indexing**  
   Each chunk is embedded using OpenAI's `text-embedding-ada-002` model and indexed with FAISS.

5. **Agent Initialization**  
   A LangChain agent is created with access to the retriever tool. You can use:
   - `ZERO_SHOT_REACT_DESCRIPTION` agent with error handling, or
   - `OPENAI_FUNCTIONS` agent for structured reasoning.

6. **User Query → Agentic Answering**  
   The user enters a natural language question. The agent retrieves top-k chunks from FAISS and generates a response grounded in those chunks using GPT.

---

### 🖥️ Demo Example

> Upload a bank agreement PDF and ask:  
> **“What is the account holder's name and interest rate mentioned?”**  
> → The app will extract and return exact information from the relevant sections of the document.

---

### 📁 Project Structure

```
📁 pdf_rag_app/
├── app.py                  # Main Streamlit app
├── rag_utils.py            # PDF extraction, chunking, embedding logic
├── agentic_rag.py          # LangChain agent setup with retriever tool
├── .env                    # OpenAI API key
├── requirements.txt        # Python dependencies
```

---

### ✅ To-Do (Enhancements)

- [ ] Add Markdown preview for extracted content
- [ ] Improve support for checkboxes and form-like layouts
- [ ] Upload multiple PDFs and tag content by metadata
- [ ] Integrate ChatMemory for multi-turn conversation
- [ ] Deploy to Streamlit Cloud

---

### 📌 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your OpenAI key to a `.env` file:
```env
OPENAI_API_KEY=your-api-key
```

3. Run the app:
```bash
streamlit run app.py
```

---

### 🙌 Credits

- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)

import streamlit as st
from rag_utils import extract_text_from_pdf, chunk_text, embed_and_store_chunks
from agentic_rag import build_agent_rag

st.set_page_config(page_title="PDF RAG Agent", layout="wide")

st.title("📄 Agentic RAG over PDFs with OpenAI")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    st.info("Extracting text from PDF...")
    text = extract_text_from_pdf(uploaded_file)
    st.success("Text extraction complete.")

    st.info("Chunking & embedding...")
    chunks = chunk_text(text)
    vector_store = embed_and_store_chunks(chunks)
    st.success("Embedding complete.")

    st.info("Initializing RAG agent...")
    agent = build_agent_rag(vector_store)
    st.success("RAG agent is ready!")

    st.subheader("Ask a question based on your PDF")
    user_query = st.text_input("Your question")

    if user_query:
        with st.spinner("Thinking..."):
            response = agent.run(user_query)
        st.write("### 🤖 Answer")
        st.write(response)

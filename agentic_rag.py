from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

def build_agent_rag(vector_store):
    retriever_tool = Tool(
        name="PDF Retriever",
        func=lambda q: "\n\n".join([doc.page_content for doc in vector_store.similarity_search(q, k=5)]),
        description="Useful for answering questions about the uploaded PDF"
    )
    
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    agent = initialize_agent(
        tools=[retriever_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent

from langchain_core.prompts import PromptTemplate

def get_base_prompt():
    return PromptTemplate(
        template="""
You are a helpful AI assistant.
Only use the provided transcript context to answer the question.
If not found in context, reply: "I don’t know."

Context:
{context}

Question: {question}
""",
        input_variables=["context", "question"]
    )

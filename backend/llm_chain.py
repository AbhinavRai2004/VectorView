from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from backend.prompts.base_prompt import get_base_prompt
from dotenv import load_dotenv

load_dotenv()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def build_chain(retriever):
    prompt = get_base_prompt()
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
    parser = StrOutputParser()

    parallel = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    return parallel | prompt | llm | parser

from backend.transcript import get_transcript, split_transcript
from backend.vectorstore import create_vector_store
from backend.llm_chain import build_chain

def process_video(video_id: str):
    raw_transcript = get_transcript(video_id)
    if not raw_transcript:
        return None, "Transcript unavailable or disabled."

    chunks = split_transcript(raw_transcript)
    vector_store = create_vector_store(chunks)
    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": 4}
    )
    chain = build_chain(retriever)
    return chain, None

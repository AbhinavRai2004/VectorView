from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def get_transcript(video_id: str):
    try:
        transcript_data = YouTubeTranscriptApi().fetch(video_id, languages=["en"]).to_raw_data()
        return " ".join(chunk["text"] for chunk in transcript_data)
    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
    except Exception as e:
        print(f"Transcript error: {e}")
    return None

def split_transcript(transcript_data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.create_documents([transcript_data])

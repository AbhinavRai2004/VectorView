import streamlit as st
from backend.core import process_video 

st.set_page_config(page_title="YouTube Chatbot", page_icon="🎥", layout="wide")

st.markdown("""
<style>
    /* Main App background */
    .stApp {
        background-color: #000010;
        color: #e0e0e0;
    }
    .chat-bubble {
        border-radius: 20px;
        padding: 12px 20px;
        margin-bottom: 14px;
        max-width: 70%;
        display: flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .user {
        background: linear-gradient(to right, #14469F, #DA3068);
        color: white;
        align-self: flex-end;
        margin-left: auto;
        # flex-direction: row-reverse;
    }
    .bot {
        background: linear-gradient(to right, #2F284E);
        align-self: flex-start;
        margin-right: 80px;
        color: #f0f0f0;
    }
    .chat-avatar {
        font-size: 24px;
    }
    /* The main container for the chat history */
    [data-testid="stVerticalBlock"] .st-emotion-cache-1c7y2kd {
        background-color: #212134;
        border-radius: 15px;
        padding: 15px;
        height: 30vh; 
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "video_id" not in st.session_state:
    st.session_state.video_id = None
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None


with st.sidebar:
    st.header("⚙️ Configuration")
    video_input = st.text_input("Enter YouTube Video ID:", key="video_input_sidebar")
    if st.button("Process Video", use_container_width=True):
        if video_input:
            with st.spinner("🔎 Processing video transcript..."):
                chain, error = process_video(video_input)
                if error:
                    st.error(error)
                else:
                    st.session_state.video_id = video_input
                    st.session_state.qa_chain = chain
                    st.session_state.messages = []
                    st.success("✅ Video processed! You can now start chatting.")
        else:
            st.warning("Please enter a Video ID.")
    st.markdown("---")
    if st.button("🔄 Start New Chat", use_container_width=True):
        st.session_state.clear()
        st.rerun()


st.title("🎥 YouTube Video Chatbot")
st.markdown("<h3 style='text-align: center; color: #a0a0c0;'>Chat with any YouTube video instantly!</h3>", unsafe_allow_html=True)

if not st.session_state.video_id:
    st.info("Please enter a YouTube Video ID in the sidebar to begin chatting.")
else:
    vid_col1, vid_col2, vid_col3 = st.columns([0.1, 0.8, 0.1])
    with vid_col2:
        st.video(f"https://www.youtube.com/watch?v={st.session_state.video_id}")

    st.markdown("---") 
    
    with st.container():
        for msg in st.session_state.messages:
            role_class = "user" if msg['role'] == 'user' else 'bot'
            avatar = "👤" if msg['role'] == 'user' else "🤖"
            st.markdown(
                f"<div class='chat-bubble {role_class}'><span class='chat-avatar'>{avatar}</span>{msg['content']}</div>",
                unsafe_allow_html=True
            )
    
    question = st.chat_input("Ask something about the video...")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.spinner("🧠 Thinking..."):
            answer = st.session_state.qa_chain.invoke(question)
        st.session_state.messages.append({"role": "bot", "content": answer})
        st.rerun()
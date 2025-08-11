import streamlit as st
from backend.core import process_video

# App Config
st.set_page_config(page_title="YouTube Chatbot", page_icon="🎥", layout="wide")

# Custom CSS Styling
st.markdown("""
<style>
    /* General App Background */
    .stApp {
        background-color: #0e0e16;
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Video Container Spacing */
    .video-container {
        margin-bottom: 20px;
    }

    /* Chat Bubble Styling */
    .chat-bubble {
        border-radius: 20px;
        padding: 12px 18px;
        max-width: 75%;
        display: flex;
        align-items: flex-start;
        gap: 10px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
        animation: fadeIn 0.3s ease-in-out;
        line-height: 1.5;
        word-wrap: break-word;
    }
    .user {
        background: linear-gradient(135deg, #14469F, #DA3068);
        color: white;
        align-self: flex-end;
        margin-bottom: 10px;
        margin-top: 10px;
        flex-direction: row-reverse;
        margin-left: auto;
    }
    .bot {
        background: #252542;
        color: #f0f0f0;
        align-self: flex-start;
        margin-right: auto;
    }

    /* Avatar Styling */
    .chat-avatar {
        font-size: 22px;
        flex-shrink: 0;
        margin-top: 3px;
    }
    
    .stTextInput > div > div > input {
            border: 2px solid #B9375D;
            border-radius: 8px;
            padding: 5px;
    }
    .example-box {
            background-color: #1E1E1E;
            border: 1px solid #F5BABB;
            border-radius: 8px;
            padding: 10px;
            margin-top: 5px;
            margin-bottom: 10px;
            font-size: 14px;
            line-height: 1.5;
    }
            
    .example-box code {
            background-color: #2E2E2E;
            padding: 2px 4px;
            border-radius: 4px;
            color: #F3E2D4;
            font-family: monospace;
    }
         
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)


# Session State Init
if "messages" not in st.session_state:
    st.session_state.messages = []
if "video_id" not in st.session_state:
    st.session_state.video_id = None
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

with st.sidebar:
    st.header("⚙️ Configuration")
    
    video_input = st.text_input("Enter YouTube Video ID:", key="video_input_sidebar")

    st.markdown(
        """
        <div class="example-box">
        💡 <b>Example:</b><br>
            For the URL <code>https://www.youtube.com/watch?v=abcd1234xyz</code>,<br>
            the Video ID is <code>abcd1234xyz</code>.
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🚀 Process Video", use_container_width=True):
        if video_input:
            with st.spinner("🔎 Fetching and processing transcript..."):
                chain, error = process_video(video_input)
                if error:
                    st.error(error)
                else:
                    st.session_state.video_id = video_input
                    st.session_state.qa_chain = chain
                    st.session_state.messages = []
                    st.success("✅ Video processed! Start chatting.")
        else:
            st.warning("Please enter a video ID.")

    st.markdown("---")
    if st.button("🔄 New Chat", use_container_width=True):
        st.session_state.clear()
        st.rerun()


# Main Title
st.title("🎥 YouTube Video Chatbot")
st.markdown("<h4 style='text-align:center; color: #a0a0c0;'>Ask questions from any YouTube video’s transcript</h4>", unsafe_allow_html=True)

# Video & Chat Area
if st.session_state.video_id:
    # Video with spacing
    col_spacer, col_video, col_spacer2 = st.columns([0.1, 0.8, 0.1])
    with col_video:
        st.markdown("<div class='video-container'>", unsafe_allow_html=True)
        st.video(f"https://www.youtube.com/watch?v={st.session_state.video_id}")
        st.markdown("</div>", unsafe_allow_html=True)

    # Chat container
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for msg in st.session_state.messages:
        role_class = "user" if msg['role'] == 'user' else 'bot'
        avatar = "👤" if msg['role'] == 'user' else "🤖"
        st.markdown(
            f"<div class='chat-bubble {role_class}'><span class='chat-avatar'>{avatar}</span>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # Input box separate from chat container
    question = st.chat_input("💬 Type your question here...")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.spinner("🧠 Thinking..."):
            answer = st.session_state.qa_chain.invoke(question)
        st.session_state.messages.append({"role": "bot", "content": answer})
        st.rerun()

# VectorView 🎥🤖

<div align="center">

Chat with any YouTube video using the power of Gemini AI.

VectorView is an interactive chatbot that extracts transcripts from YouTube videos, processes them using LangChain and Google's Gemini AI, and generates accurate, context-aware responses. Built with a clean Streamlit UI, it provides an intuitive way to query video content using natural language.

</div>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
<img src="https://img.shields.io/badge/Streamlit-1.35.0-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
<img src="https://img.shields.io/badge/LangChain-0.2.0-purple?style=for-the-badge" alt="LangChain">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---
## ✨ Key Features

- 💬 **Interactive Chat Interface**: Ask questions about the video in plain English.
- 🧠 **Intelligent Q&A**: Leverages Google's Gemini Pro for high-quality, contextual answers.
- ⚡ **Fast Semantic Search**: Uses FAISS for efficient similarity searches on video content.
- 🧩 **Modular Architecture**: Clean separation between the Streamlit UI and the backend processing logic.

---


## 🛠️ How It Works

The application follows a streamlined, multi-step process to deliver answers from video content:

1. **Id Input**: The user provides a YouTube video Id through the Streamlit interface.
2. **Transcript Fetching**: The `youtube-transcript-api` is used to extract the full transcript of the video.
3. **Text Chunking**: The transcript is broken down into smaller, manageable chunks to fit the model's context window.
4. **Embedding Generation**: Each chunk is converted into a numerical vector using `HuggingFaceInstructEmbeddings`. These embeddings capture the semantic meaning of the text.
5. **Vector Storage**: The embeddings are stored in a FAISS (Facebook AI Similarity Search) in-memory vector store for ultra-fast retrieval.
6. **User Query**: The user asks a question (e.g., "What did the speaker say about AI in gaming?").
7. **Semantic Search**: The user's query is embedded, and FAISS performs a similarity search to find the most relevant text chunks from the video.
8. **LLM Augmentation**: The relevant chunks (context) and the user's query are passed to the Gemini Pro model via a LangChain QA chain.
9. **Answer Generation**: Gemini generates a human-like answer based on the provided context, which is then displayed in the UI.

---

## 🔧 Tech Stack

| Component     | Technology           | Purpose                                           |
|--------------|----------------------|---------------------------------------------------|
| Frontend     | Streamlit            | Building the interactive web UI.                 |
| LLM Framework| LangChain            | Orchestrating the entire QA chain.               |
| LLM          | Google Gemini Pro    | Core model for question answering and summarization. |
| Embeddings   | HuggingFace          | Generating text embeddings.                      |
| Vector Store | FAISS                | Storing and searching text embeddings efficiently.|
| API          | YouTube Transcript API | Fetching video transcripts.                     |

---

## ⚙️ Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites

- Python 3.10+
- Git
- A Google API Key with the Gemini API enabled (from Google AI Studio).

### 2. Clone the Repository

```bash
git clone https://github.com/AbhinavRai2004/VectorView.git
cd VidWhiz
```

### 3. Set Up a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a file named `.env` in the root directory and add your Google API Key:

```env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

### 6. Run the Application

```bash
streamlit run main_ui.py
```

Visit `http://localhost:8501` in your browser.

---

## 🗺️ Roadmap & Future Enhancements

- [ ] Multi-Video History: Implement memory to allow follow-up questions across different videos.
- [ ] Chat Persistence: Integrate a database (e.g., SQLite) to save and load chat history.
- [ ] User Authentication: Add user accounts for a personalized experience.
- [ ] Support for More Sources: Extend functionality to process articles and PDFs.
- [ ] Dockerize Application: Create a Dockerfile for easy deployment.

---

## 🙌 Acknowledgments

A big thank you to the developers and communities behind these incredible tools:

- Google Gemini
- LangChain
- Streamlit
- HuggingFace

---

### 💙 Made with love by [Abhinav Rai](https://github.com/AbhinavRai2004) 💙

# 🧠 QUIZZER

An AI-powered quiz generation application built with **Python, Streamlit, Ollama, Gemma 3, LangChain, Hugging Face Embeddings, and ChromaDB**.

QUIZZER allows users to generate interactive multiple-choice quizzes either from a general topic using AI or directly from their own PDF documents using a **Retrieval-Augmented Generation (RAG)** pipeline.

---

## 🚀 Features

### 🎯 General AI Quiz

Generate quizzes on almost any topic using the Gemma 3 model.

- Enter any topic or concept
- Customize the quiz title
- Choose difficulty: Easy, Medium, or Hard
- Generate 5–30 questions
- Four options per question
- Automatic answer evaluation
- Score and accuracy calculation
- Detailed explanations
- Topic/concept identification

### 📚 PDF-Based RAG Quiz

Generate quizzes from your own study material.

Users can upload multiple PDFs such as:

- Lecture notes
- Textbooks
- Research papers
- Technical documents
- Exam preparation material

The RAG pipeline retrieves relevant information from the uploaded documents before generating questions.

### 📊 Interactive Quiz Interface

- Question-by-question navigation
- Progress indicator
- Answer selection
- Automatic scoring
- Accuracy calculation
- Question-wise result review
- Correct answers
- Explanations
- Topic information
- Source and page information for RAG-generated questions

---

## 🧠 RAG Pipeline

```text
PDF Upload
    ↓
PDF Text Extraction
    ↓
Document Chunking
    ↓
Hugging Face Embeddings
    ↓
ChromaDB Vector Store
    ↓
MMR Retrieval
    ↓
Relevant Document Chunks
    ↓
Gemma 3
    ↓
Structured JSON Quiz
    ↓
Interactive Quiz
    ↓
Results & Explanations
```

The RAG generator is instructed to use only the retrieved document context when creating questions.

Each RAG-generated question can also contain:

- Tested concept
- Explanation
- Source document
- Page number

This helps keep the generated quiz grounded in the uploaded study material.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Streamlit | Web application interface |
| Ollama | Local LLM runtime |
| Gemma 3 4B | Quiz generation |
| LangChain | RAG pipeline |
| Hugging Face | Text embeddings |
| ChromaDB | Vector database |
| PyPDF | PDF processing |

---

## ☁️ Deployment

The current version uses **Ollama + Gemma 3 locally**.

The application can run successfully in a local environment where Ollama is installed and running.

However, the current Ollama-based version cannot be directly demonstrated through Streamlit Cloud because Streamlit Cloud does not provide the required Ollama runtime.

A future deployment can solve this by replacing the local Ollama dependency with a cloud-hosted LLM or a separate backend running Ollama.

Possible deployment architecture:

```text
Streamlit Frontend
        ↓
Cloud Backend
        ↓
LLM / Ollama Server
        ↓
Gemma
```

Platforms such as Railway or other cloud infrastructure can be considered for hosting the backend.

---

## 🔮 Future Improvements

Planned improvements may include:

- Cloud-based LLM deployment
- Public live demo
- User accounts
- Quiz history
- Personalized quizzes
- Timer-based quizzes
- Performance analytics
- Improved question validation
- Advanced retrieval strategies
- Support for additional document formats
- AI-powered study recommendations

The current version focuses on the core quiz-generation and RAG functionality, while these improvements can be added in future updates.

---

## 🎥 Live Demo

**Live Demo:**  
`[Live Demo](https://quizzer-bw4ourecvspedm6pzkxmfa.streamlit.app/)`

> Currently unavailable because the deployed Streamlit environment does not provide the Ollama runtime required by the current version.

---

## 🔗  Links

**LinkedIn:**  
`[LinkedIn](https://www.linkedin.com/in/sayan-das-1466b1369/)`

---

## 👨‍💻 Author

**Sayan Das**  
B.Tech — Petroleum Engineering  
IIT (ISM) Dhanbad



---


# 🧠 QUIZZER — AI-Powered Quiz Generator

QUIZZER is an AI-powered quiz generation application that creates customized multiple-choice quizzes from any general topic or from user-provided PDF documents.

It combines Large Language Models, Retrieval-Augmented Generation (RAG), vector embeddings, semantic retrieval, and Streamlit to provide an interactive quiz experience with automatic evaluation and explanations.

## 🚀 Live Demo

**Live Demo:** [(https://quizzer-bw4ourecvspedm6pzkxmfa.streamlit.app/)]

---

## ✨ Features

### 🎯 AI-Powered Topic Quizzes

- Generate quizzes from any topic or concept.
- Choose between Easy, Medium, and Hard difficulty.
- Select 5–30 questions.
- Generate four-option multiple-choice questions.
- Automatic answer evaluation.
- Detailed explanations for every question.
- Interactive question-by-question quiz interface.

### 📚 PDF-Based RAG Quizzes

QUIZZER can generate quizzes directly from user-provided study material.

The application supports:

- Uploading multiple PDF documents.
- Extracting text from PDFs.
- Splitting documents into meaningful chunks.
- Generating vector embeddings using Hugging Face.
- Storing embeddings in ChromaDB.
- Retrieving relevant document content using Maximal Marginal Relevance (MMR).
- Generating questions using the retrieved document context.
- Including source file and page information in generated questions.
- Preventing the model from relying on outside knowledge for document-based questions.

### 📊 Quiz Evaluation

After completing a quiz, users receive:

- Total score
- Accuracy percentage
- Question-by-question results
- User's answer
- Correct answer
- Explanation

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama
- Gemma 3 4B
- LangChain
- Hugging Face Embeddings
- ChromaDB
- PyPDF

---

## 🧠 How It Works

For general topic quizzes, the user provides a topic, difficulty, title, and number of questions. The application sends these requirements to the locally running Gemma 3 4B model, which generates a structured JSON quiz that is displayed through the Streamlit interface.

For PDF-based quizzes, the uploaded documents are processed through a RAG pipeline. The PDF text is extracted, split into chunks, converted into embeddings, and stored in ChromaDB. Relevant chunks are retrieved using MMR and passed to Gemma 3 4B as context. The model then generates questions based only on the retrieved document information.

The complete workflow is:

User Input → Quiz Configuration → AI/RAG Processing → Quiz Generation → Interactive Quiz → Automatic Evaluation → Results

---


## 🔍 RAG Pipeline

The PDF quiz generation system follows a Retrieval-Augmented Generation architecture:

PDF Documents → PDF Loader → Text Splitting → Embeddings → ChromaDB → MMR Retrieval → Relevant Context → Gemma 3 4B → Structured Quiz → User Evaluation

This allows QUIZZER to generate questions grounded in the uploaded documents rather than depending entirely on the model's general knowledge.

The retrieval system uses Maximal Marginal Relevance to retrieve relevant and diverse document chunks, helping the generated quiz cover different concepts from the available material.

---

## 🎓 Use Cases

QUIZZER can be used for:

- Exam preparation
- Academic revision
- Technical interview preparation
- Textbook-based quizzes
- Research paper comprehension
- Lecture note revision
- Petroleum engineering study
- General knowledge practice

---

## 🔮 Future Improvements

Possible future improvements include:

- Personalized question difficulty
- Improved question diversity
- Better retrieval optimization
- Quiz history and performance tracking
- Additional document formats
- Faster quiz generation
- Performance analytics
- Improved UI and user experience

---

## 👨‍💻 Author

Sayan Das

B.Tech — Petroleum Engineering  
IIT (ISM) Dhanbad

LinkedIn: [[Your LinkedIn Profile](https://www.linkedin.com/in/sayan-das-1466b1369/)]



---

⭐ If you find QUIZZER useful, consider giving the repository a star!

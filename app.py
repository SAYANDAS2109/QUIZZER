import streamlit as st
from quiz.generator import generate_general_quiz
from quiz.rag.rag_generator import generate_rag_quiz
from quiz.rag.process import process_uploaded_pdfs

st.set_page_config(
    page_title="QUIZZER",
    page_icon="🧠",
    layout="wide"
)

#Session state

if "page" not in st.session_state:
    st.session_state.page = "home"
if "quiz" not in st.session_state:
    st.session_state.quiz = None
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers ={}
if "quiz_mode" not in st.session_state:
    st.session_state.quiz_mode = None
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

#HOMEEEEEE

def show_home():
    st.title("🧠 QUIZZER")

    st.write(
        "Create quizzes from any topic or from your own PDF documents."
    )

    st.divider()

    st.subheader("🎯 Choose your quiz source")
    col1,col2 = st.columns(2,gap="large")

    # st.subheader("🎯 Choose your quiz source")

    with col1:
        with st.container(border=True):
            st.subheader("🎯 General AI")
            st.caption("Quick Quiz")
            st.write(
            "Generate questions from any topic or concept "
                "using the AI's general knowledge."
        )
            st.write("")
            st.markdown("**Suitable for:**")
            st.write(
                "• General knowledge\n"
                "• Academic concepts\n"
                "• Interview preparation\n"
                "• Quick revision"
            )
            if st.button(
            "⚡Topic Quiz",
            use_container_width=True,
            type="primary"
            ):
                st.session_state.page = "general_config"
                st.session_state.quiz_mode = "general"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.subheader("📚Documents")
            st.caption("RAG Powered Quiz")
            st.write(
                "Upload PDFs and generate questions from your study material!!!!."
            )
            st.write("")

            st.markdown("**Best for:**")

            st.write(
                    "• Lecture notes\n"
                    "• Textbooks\n"
                    "• Research papers\n"
                    "• Exam preparation"
                )
            if st.button(
                "Quiz from PDF",
                use_container_width=True,
                type="primary"
            ):
                st.session_state.page = "pdf_config"
                st.session_state.quiz_mode="pdf"
                st.rerun()


#General AI configurationnnnn

def show_general_config():
    st.title("💥Create a Topic Quiz")
    st.caption(
        "Tell QUIZZER what you want to learn and customize your quiz."
    )
    st.divider()
    with st.container(border=True):
        st.subheader("QUIZ INFO📍")
        topic = st.text_input(
        "Topic/Concept",
        placeholder="e.g. Reservoir Engineering Fundamentals"
    
    )
        title = st.text_input(
        "Quiz Title",
        placeholder="e.g. RESERVOIR QUIZ"
    )
    with st.container(border=True):
        st.subheader("Quiz Configuration✨")
        col1,col2 = st.columns(2)
        with col1:
            difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            'Hard'
        ]
    )
        with col2:

            num_questions = st.selectbox(
        "Number of Questions",
        [5,10,15,20,25,30]
    )
    st.write()
    
    col1,col2 = st.columns(2)
    with col1:
        if st.button(
            "<- HOME",
            use_container_width=True
        ):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        generate = st.button(
            "GENERATE QUIZZZ⚡",
            use_container_width=True,
            type="primary"
        )
    if generate:
        if not topic.strip():
            st.error('Please enter a Topic')

            return
        if not title.strip():
            title = f"{topic} Quiz"
        with st.spinner("Generating your quiz..."):
            try:
                quiz = generate_general_quiz(
                    topic=topic,
                    title=title,
                    difficulty=difficulty,
                    num_questions=num_questions
                )

                st.session_state.quiz = quiz
                st.session_state.current_question = 0
                st.session_state.answers = {}
                st.session_state.page = "quiz"

                st.rerun()
            except Exception as e:
                st.error(
                    f"Genration failed: {e}"
                
                )

#Pdf configgggg

def show_pdf_config():
    st.title("📚Create Quiz from Documents")
    st.caption(
        "Upload your study material and QUIZZER will use RAG "
        "to create questions from it."
    )
    st.divider()
    with st.container(border=True):
        st.subheader("Upload Study Material📃")
        uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )
        if uploaded_files:
            st.success(f"{len(uploaded_files)} PDF(s) uploaded."
        )
        st.write("")
        if st.button(
            "⚙️ PROCESS DOCUMENTS",
                use_container_width=True,
                type="primary"
        ):
            with st.spinner(
                    "Processing documents and building RAG index..."
                ):
                    try:
                        vectorstore = process_uploaded_pdfs(
                            uploaded_files
                        )

                        st.session_state.vectorstore = vectorstore
                        st.session_state.pdf_processed = True

                        st.success(
                            "✅ Documents processed successfully!"
                        )

                    except Exception as e:

                        st.session_state.vectorstore = None
                        st.session_state.pdf_processed = False

                        st.error(
                            f"Document processing failed: {e}"
                        )
        else:
            st.info(
                "Upload one or more PDF files to continue."
            )
            
    if st.session_state.pdf_processed:
        st.divider()
        st.success(
            "🟢 RAG is ready. Your documents can now be used "
            "to generate the quiz."
        )
    st.write("")
    with st.container(border=True):
        st.subheader("Quiz Info📍")
        title= st.text_input(
        "Quiz Title",
        placeholder="Petro Quizzz",
        key="pdf_title"
    )
    st.write("")
    with st.container(border=True):
        st.subheader("Quiz Configuration💥")
        col1,col2 =st.columns(2)
        with col1:
            difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )
        with col2:
            num_questions = st.selectbox(
        "Number of Questions",
        [5,10,15,20,25,30],
        key= "pdf_num_questions"
    )
    st.write("")
    col1,col2 = st.columns(2)
    with col1:
        if st.button(
                "<- HOME",
                use_container_width=True
        ):  
            st.session_state.page = "home"
            st.rerun()
    with col2:
        generate = st.button(
                    "GENERATE QUIZZZ⚡",
                    use_container_width=True,
                    type="primary",
                    disabled=not st.session_state.pdf_processed
                )
    if generate:
        if not title.strip():
            title = "Document Quiz"
        with st.spinner(
            "🔎 Retrieving relevant content and generating quiz..."
        ):
            try:
                quiz = generate_rag_quiz(

                    vectorstore=st.session_state.vectorstore,

                    title=title,

                    difficulty=difficulty,

                    num_questions=num_questions,

                    query=(
                        "Identify the important concepts, "
                        "definitions, principles, mechanisms, "
                        "relationships and factual information "
                        "covered in the uploaded documents."
                    )
                )
                st.session_state.quiz = quiz

                st.session_state.current_question = 0

                st.session_state.answers = {}

                st.session_state.page = "quiz"

                st.rerun()

            except Exception as e:
                st.error(
                    f"Quiz generation failed:{e}"
                )

#  INTERFACEEEEEEEEE

def show_quiz():
    quiz = st.session_state.quiz

    if not quiz:
        st.session_state.page = "home"
        st.rerun()
    questions = quiz["questions"]
    index = st.session_state.current_question
    question = questions[index]
    st.title(quiz["title"])

    st.progress(
        (index + 1) / len(questions)
    )

    st.write(
        f"Question {index + 1} of {len(questions)}"
    )

    with st.container(border=True):
        st.subheader(
            question["question"]
        )
        answer = st.radio(
            "Select your answer:",
            question["options"],
            index=None,
            key=f"question_{index}"
        )

        st.divider()

        if index < len(questions) - 1:

            if st.button(
                "Next -->",
                type="primary",
                use_container_width=True
            ):
                if answer is None:
                    st.warning(
                        "Please answer this question before continuing"
                    )
                else:
                    st.session_state.answers[index] = answer
                    st.session_state.current_question += 1

                    st.rerun()

        else:
            if st.button(
                "Submit QUIZZZZ",
                type="primary",
                use_container_width=True
            ):
                if answer is None:
                    st.warning(
                        "Please answer this question before submitting."
                    )

                else:
                    st.session_state.answers[index] = answer
                    st.session_state.page = "results"

                    st.rerun()


#RESULTSS

def show_results():
    quiz = st.session_state.quiz
    answers = st.session_state.answers

    questions = quiz["questions"]

    score = 0

    for i, question in enumerate(questions):

        if answers.get(i) == question["correct_answer"]:

            score += 1

    percentage = (score / len(questions)) * 100

    st.title('Quiz Completed🎉🎊')

    st.metric(
        "Score",
        f"{score}/{len(questions)}"
    )

    st.metric(
        "Accuracy",
        f"{percentage:.2f}%"
    )

    st.divider()

    for i, question in enumerate(questions):

        user_answer = answers.get(i)

        if user_answer == question["correct_answer"]:

            st.success(
                f"Question {i + 1} — Correct"
            )

        else:

            st.error(
                f"Question {i + 1} — Incorrect"
            )

        st.write(
            question["question"]
        )

        st.write(
            f"**Your answer:** {user_answer}"
        )

        st.write(
            f"**Correct answer:** "
            f"{question['correct_answer']}"
        )

        st.write(
            f"**Topic:** {question['topic']}"
        )

        st.write(
            f"**Explanation:** {question['explanation']}"
        )

        st.divider()
    col1,col2 =st.columns(2)

    with col1:
        if st.button(
            "HOME🏠",
            use_container_width=True
        ):
            st.session_state.page = "home"
            st.session_state.quiz = None
            st.rerun()

    with col2:
        if st.button(
            "NEXT QUIZZZZ😼",
            use_container_width=True,
            type='primary'

        ):
            if st.session_state.quiz_mode=="pdf":
                st.session_state.page = "pdf_config"
            else:
                st.session_state.page = "general_config"
           
            st.session_state.quiz = None
            st.session_state.answers = {}
            st.session_state.current_question = 0

            st.rerun()

#page router

if st.session_state.page == "home":

    show_home()

elif st.session_state.page == "general_config":

    show_general_config()

elif st.session_state.page == "pdf_config":

    show_pdf_config()

elif st.session_state.page == "quiz":

    show_quiz()

elif st.session_state.page == "results":

    show_results()




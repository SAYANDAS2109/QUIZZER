import os
import tempfile

from quiz.rag.loader import load_pdf
from quiz.rag.splitter import split_documents
from quiz.rag.vectorstore import create_vectorstore


def process_uploaded_pdfs(uploaded_files):

    if not uploaded_files:
        raise ValueError(
            "Please upload at least one PDF"
        )

    temp_dir = tempfile.mkdtemp()

    all_documents = []

    for uploaded_file in uploaded_files:

        file_path = os.path.join(
            temp_dir,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )

        documents = load_pdf(file_path)

        all_documents.extend(documents)

    if not all_documents:
        raise ValueError(
            "No text could be extracted from the PDFs."
        )

    chunks = split_documents(
        all_documents
    )

    if not chunks:
        raise ValueError(
            "No chunks were created from the PDFs."
        )

    vectorstore = create_vectorstore(
        chunks,
        persist_directory=os.path.join(
            temp_dir,
            "chroma"
        )
    )

    return vectorstore
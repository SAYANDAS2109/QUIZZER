from quiz.rag.embeddings import get_embedding_model
from langchain_chroma import Chroma


def load_vectorstore(persist_directory):
    embeddings = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    return vectorstore


def retrieve_documents(
    query,
    vectorstore,
    k=20
):
    documents = vectorstore.max_marginal_relevance_search(
        query,
        k=k,
        fetch_k=50,
        lambda_mult=0.5
    )

    return documents
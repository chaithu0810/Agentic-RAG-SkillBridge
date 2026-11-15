
from pathlib import Path

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import FAISS


POLICY_FOLDER = Path("policies")
VECTOR_FOLDER = "vector_store"

EMBEDDING_MODEL = "nomic-embed-text"


def get_embeddings():

    return OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )


def create_vector_store():

    print("Loading policy documents...")

    if not POLICY_FOLDER.exists():
        raise FileNotFoundError(
            "Policies folder not found"
        )

    loader = DirectoryLoader(
        str(POLICY_FOLDER),
        glob="*.md",
        loader_cls=TextLoader,
        loader_kwargs={
            "encoding": "utf-8"
        },
        show_progress=True
    )

    documents = loader.load()

    if not documents:
        raise ValueError(
            "No Markdown policy files found"
        )

    print("Documents loaded:", len(documents))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
        separators=[
            "\n# ",
            "\n## ",
            "\n\n",
            "\n",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(documents)

    if not chunks:
        raise ValueError(
            "No document chunks generated"
        )

    print("Chunks created:", len(chunks))

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(
        VECTOR_FOLDER
    )

    print("FAISS index saved successfully")

    return vector_store


def load_vector_store():

    index_path = (
        Path(VECTOR_FOLDER) / "index.faiss"
    )

    embeddings = get_embeddings()

    if index_path.exists():

        print("Loading existing FAISS index...")

        return FAISS.load_local(
            VECTOR_FOLDER,
            embeddings,
            allow_dangerous_deserialization=True
        )

    return create_vector_store()


def search_policy(question: str):

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 3,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )

    documents = retriever.invoke(question)

    results = []

    for doc in documents:

        results.append({

            "content": doc.page_content,

            "source": Path(
                doc.metadata.get(
                    "source",
                    "Unknown"
                )
            ).name

        })

    return results


def rebuild_policy_index():

    import shutil

    if Path(VECTOR_FOLDER).exists():

        shutil.rmtree(VECTOR_FOLDER)

    return create_vector_store()

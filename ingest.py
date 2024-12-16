import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_PATH = 'data/'  # Path to data folder containing PDFs
DB_FAISS_PATH = 'vectorstore/db_faiss'  # Where to save the vector store

# Create vector database
def create_vector_db():
    loader = DirectoryLoader(DATA_PATH,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)  # Loading PDFs

    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    # Modify file path to use a local server or file protocol
    for doc in documents:
        # Get the absolute file path of the PDF
        file_path = os.path.abspath(doc.metadata.get("source", "unknown"))
        
        relative_path = os.path.relpath(file_path, DATA_PATH)
        doc.metadata["file_path"] = f"http://localhost:8001/{relative_path.replace(os.sep, '/')}"

    # Create vector store
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()

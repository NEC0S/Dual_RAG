from data_sources.pdf_handler import PDFHandler
from data_sources.url_handler import URLHandler
from data_sources.text_handler import TextHandler
from llama_index.core import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex
import data_sources.data_dump as data_dump

class DataSourceManager:
    def __init__(self):
        self.pdf_handler = PDFHandler(data_dump.PDF_FILES)
        self.url_handler = URLHandler(data_dump.URLS)
        self.text_handler = TextHandler(data_dump.TEXT_FILES)
        self.documents = []

    def load_all_data(self):
        self.documents.extend(self.pdf_handler.load_data())
        self.documents.extend(self.url_handler.load_data())
        self.documents.extend(self.text_handler.load_data())
        return self.documents

    def create_index(self):
        # Embedding model
        embed_model = HuggingFaceEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )
        # Create a VectorStoreIndex from the documents
        index = VectorStoreIndex.from_documents(self.documents, embed_model=embed_model)
        return index

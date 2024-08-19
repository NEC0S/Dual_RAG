
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from data_sources.data_dump import DataDump
from llama_index.core import Settings


class ChatBot1:
    def __init__(self):
        # Initialize the LLM
        self.llm = Ollama(model="llama2", request_timeout=600)
        
        # Explicitly set the embedding model to HuggingFace
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        Settings.embed_model = self.embed_model  # Ensure the correct embedding model is used

        # Explicitly set the LLM in the global settings
        Settings.llm = self.llm

        self.data = DataDump().load_data1()

        # Create the index and chat engine
        self.index = VectorStoreIndex.from_documents(self.data)
        self.chat_app = self.index.as_chat_engine(chat_mode="condense_plus_context")

    def get_response(self, query):
        response = self.chat_app.chat(query)
        return response.response
    

class ChatBot2:
    def __init__(self):
        # Initialize the LLM
        self.llm = Ollama(model="llama2", request_timeout=600)
        
        # Explicitly set the embedding model to HuggingFace
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        Settings.embed_model = self.embed_model  # Ensure the correct embedding model is used

        # Explicitly set the LLM in the global settings
        Settings.llm = self.llm

        self.data = DataDump().load_data2()

        # Create the index and chat engine
        self.index = VectorStoreIndex.from_documents(self.data)
        self.chat_app = self.index.as_chat_engine(chat_mode="condense_plus_context")

    def get_response(self, query):
        response = self.chat_app.chat(query)
        return response.response
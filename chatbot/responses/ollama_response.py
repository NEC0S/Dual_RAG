from .base_response import BaseResponse
from llama_index.llms.ollama import Ollama

class OllamaResponse(BaseResponse):
    def __init__(self):
        self.llm = Ollama(model="llama2", request_timeout=600)

    def get_response(self, query):
        return self.llm.chat(query).response

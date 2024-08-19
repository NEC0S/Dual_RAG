from abc import ABC, abstractmethod
from llama_index.core import Document

class BaseHandler(ABC):
    @abstractmethod
    def load_data(self):
        pass

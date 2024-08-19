from llama_index.core import Document

class TextHandler:
    def load_texts(self):
        text_files = [
            # Add paths to your text files here
        ]
        docs = []
        for text_file in text_files:
            with open(text_file, 'r') as file:
                text = file.read()
                docs.append(Document(text=text, metadata={"source": text_file}))
        return docs

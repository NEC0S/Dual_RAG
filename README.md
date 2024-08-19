# Chatbot 

This project implements a modular and scalable chatbot using Flask and the Ollama LLM model. The chatbot is designed to be easily extendable, with separate components for handling different data sources and generating responses.

## File Structure

```plaintext
chatbot_project/
│
├── app.py
├── chatbot/
│   ├── __init__.py
│   ├── chatbot.py 
│   └── responses/
│       ├── __init__.py
│       ├── base_response.py
│       └── ollama_response.py
│
├── data_sources/
│   ├── __init__.py
│   ├── base_handler.py
│   ├── pdf_handler.py
│   ├── url_handler.py
│   ├── data_dump.py
│   ├── data_source_manager.py
│   └── text_handler.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── styles.css
├── user_data/
│   └── data.csv
│       
├── requirements.txt
└── README.md
```
## Directory and File Descriptions

- **`app.py`**: The main entry point for the Flask application. It sets up the routes and initializes the chatbot.

- **`chatbot/`**: Contains the core logic for the chatbot.
  - **`chatbot.py`**: Manages the chatbot's state and processes user input.
  - **`responses/`**: Contains different response generators.
    - **`base_response.py`**: A base class for all response generators.
    - **`ollama_response.py`**: Implements the response generation logic using the Ollama LLM model.

- **`data_sources/`**: Handles data fetching from different sources.
  - **`base_handler.py`**: A base class for data handlers.
  - **`pdf_handler.py`**: Handles data from PDF files.
  - **`url_handler.py`**: Handles data from URLs.
  - **`text_handler.py`**: Handles data from text files.

- **`templates/`**: Contains HTML templates for the web interface.
  - **`index.html`**: The main HTML file for the chatbot interface.

- **`static/css/`**: Contains static files such as CSS.
  - **`styles.css`**: Custom styles for the chatbot interface.

- **`requirements.txt`**: Lists all the dependencies required for the project.

- **`README.md`**: This file, providing an overview of the project, structure, and usage instructions.

## Modifying the Model

If you want to change the model used by the chatbot, follow these steps:

1. **Create a New Response Generator Class**:
   - Navigate to the `chatbot/responses/` directory and create a new file, e.g., `new_model_response.py`.
   - Implement the new model logic in this file by subclassing `BaseResponse`.

   ```python
   from .base_response import BaseResponse

   class NewModelResponse(BaseResponse):
       def __init__(self):
           # Initialize your new model here
           pass

       def generate_response(self, user_input):
           # Implement response generation using the new model
           return "Response from the new model"

## Update `chatbot.py`

To integrate the new model into the chatbot, follow these steps:

1. **Open the `chatbot/chatbot.py` file**:
   - Locate the `chatbot/chatbot.py` file in your project directory and open it in your code editor.

2. **Import your new response generator class**:
   - Add an import statement at the top of the `chatbot.py` file to include your new response generator class:

   ```python
   from .responses.new_model_response import NewModelResponse


## Example

Here's an example image related to the project:

![image](https://github.com/user-attachments/assets/f4b7aefa-ff76-40d7-bf65-1171413f3e49)

## Issues with the Model

### 1. Very Slow Performance

#### Problem
The model might be running slowly due to several factors:
- **Large Size of Documents**: Processing large documents or a large number of documents can lead to slow response times.
- **Complexity of the Model**: Large language models (LLMs) with significant computational requirements may have inherently slow inference times.
- **Open Source Model**: Using Open-source model can also affect performance, also Limited hardware resources, such as insufficient RAM or GPU power can be potential reasons.


### 2. Responses Too Specific to Documents

#### Problem
The model may generate responses that are overly specific to the given document rather than providing general or diverse responses.


### Solutions

- **Chunk Documents**: Break down large documents into smaller chunks or sections to reduce the load on the model.

- **Scale Resources**: Consider using distributed computing or cloud services to handle larger workloads.

- **Optimize Model Usage**:
  - **Use Faster Models**: Evaluate if a lighter or faster model could meet your needs without compromising much on quality.
  - **Reduce Model Size**: If feasible, use a smaller version of the model to improve performance.



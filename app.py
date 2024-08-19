from flask import Flask, render_template, request, jsonify
from chatbot.chatbot import ChatBot1, ChatBot2

app = Flask(__name__)

# Instantiate your chatbots
chatbot1 = ChatBot1()
chatbot2 = ChatBot2()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot1', methods=['POST'])
def chatbot1_response():
    data = request.json
    query = data.get('query')
    response = chatbot1.get_response(query)
    return jsonify({"response": response})

@app.route('/chatbot2', methods=['POST'])
def chatbot2_response():
    data = request.json
    query = data.get('query')
    response = chatbot2.get_response(query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

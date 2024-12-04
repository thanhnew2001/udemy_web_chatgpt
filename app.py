from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

openai.api_key = "xxxx"

app = Flask(__name__)

CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data["question"]
    reply = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
    ]
    )
    answer = reply["choices"][0]["message"]["content"]
    return jsonify({"answer": answer})

app.run()

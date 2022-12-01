import urllib
from urllib import parse

from flask import Flask
from flask import request
import ai
import uuid

app = Flask(__name__)

conversations = {}


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")


@app.route("/new_conversation/", methods=["POST"])
@app.route("/new_conversation/<conversation_id>", methods=["POST"])
def new_conversation(conversation_id=None):
    if conversation_id is None:
        conversation_id = str(uuid.uuid4())

    # if conversation_id already exists, return error
    if conversation_id in conversations:
        return {"error": f"conversation_id: {conversation_id} already exists"}

    conversation = ai.Conversation(ai.searchEnginePrompt)
    conversations[conversation_id] = conversation
    return {"conversation_id": conversation_id}


@app.route("/conversation/<conv_id>", methods=["POST", "PUT"])
def prompt(conv_id: str):
    # get prompt from request body from json key "prompt"
    p = request.get_json()["prompt"]
    print(f"Getting response for prompt: {p} ...")
    if conv_id not in conversations:
        return {"error": f"conversation_id: {conv_id} does not exist"}

    (conversation, next_prompt) = conversations[conv_id].get_next_prompt(p)
    print(f"Next prompt: {next_prompt}")
    response = ai.get_response(ai.searchEnginePrompt + p).choices[0].text
    # response = "AI: Mock response with subject 1, subject 2 and subject 3" \
    #            "Subjects: |mock subject 1|mock subject 2|mock subject 3|"
    print(response)
    response_text = ai.parse_response_only(response)
    subjects = ai.parse_subjects_from_response(response)

    return {
        "response": response_text,
        "subjects": subjects,
        "search_links": [f"https://www.google.com/search?q={urllib.parse.quote_plus(subject)}" for subject in subjects]
    }


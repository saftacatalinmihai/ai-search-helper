import os
import time
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
    app.logger.info(f"Getting response for prompt: {p} ...")
    if conv_id not in conversations:
        return {"error": f"conversation_id: {conv_id} does not exist"}

    (conversation, next_prompt) = conversations[conv_id].get_next_prompt(p)
    app.logger.info(f"Getting response for conversation: {next_prompt} ...")

    # IF the MOCK env variable is set to true, then return a mock response
    if os.environ.get("MOCK") == "true":
        app.logger.warn("Returning mock response")
        # sleep for 1 second to simulate a slow response
        time.sleep(1)
        response = "AI: Mock response with subject 1, subject 2 and subject 3\nSubjects: |mock subject 1|mock subject 2|mock subject 3|"
    else:
        response = ai.get_response(next_prompt).choices[0].text
        conversation.add_response(response)

    app.logger.info(f"Response: {response}")
    response_text = ai.parse_response_only(response)
    app.logger.info(f"Response text: {response_text}")
    subjects = ai.parse_subjects_from_response(response)

    return {
        "response": response_text,
        "subjects": subjects,
        "search_links": [f"https://www.google.com/search?q={urllib.parse.quote_plus(subject)}" for subject in subjects]
    }


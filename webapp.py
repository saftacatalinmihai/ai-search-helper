from flask import Flask
from flask import request
import llm
from flask import render_template

app = Flask(__name__)


@app.route("/prompt")
def prompt():
    p = request.args.get("prompt")
    response = llm.get_response(llm.searchEnginePrompt + p).choices[0].text
    print(response)
    response_text = llm.parse_response_only(response)
    subjects = llm.parse_subjects_from_response(response)

    # response_text = "test"
    # subjects = ["test"]

    # search_links = [f"https://www.google.com/search?q={urllib.parse.quote_plus(subject)}" for subject in subjects]
    return render_template('prompt.html',
                           prompt=p,
                           response_text=response_text,
                           subjects=subjects,
                           )
    # return f"<p>Prompt: {p}</p>" \
    #        f"<p>Response: {response_text}</p>" \
    #        f"<p>Subjects: {subjects}</p>" \
    #        f"<div>" \
    #        f"   <p>Subjects links</p>" \
    #        f"   <ul>" \
    #        ' '.join([f"<li><a href='{link}'>{link}</a></li>" for link in search_links]) + f"</div>"


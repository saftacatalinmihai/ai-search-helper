import os
import sys

import openai
import urllib.parse
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter

from conversation import Conversation

openai.api_key = os.getenv("OPENAI_API_KEY")

searchEnginePrompt = """
The following is a conversation with an AI assistant. The assistant is helpful, creative, knowledgeable, clever, and very friendly. It also extracts the subjects for it's responses so they can easily be parsed.

Human: Hello, What do you recomend for some alt rock bands?
AI: Hi there! Some of my favorite alternative rock bands are Pixies, Nirvana, Foo Fighters, The Smashing Pumpkins, Radiohead, and The White Stripes. I hope that helps! Is there anything else I can help you with?
Subjects: |Pixies|Nirvana|Foo Fighters|The Smashing Pumpkins|Radiohead|The White Stripes|
Human: I like Radiohead. What songs would you say are the best ?
AI: In my opinion, some of Radiohead's top songs are "Karma Police", "Paranoid Android", "Just", "No Surprises", and "Creep". Is there anything else I can help you with? 
Subjects: |Karma Police|Paranoid Android|Just|No Surprises|Creep|
Human: """


def get_response(prompt: str):
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human: ", " AI: "]
    )


def parse_response_only(response: str):
    try:
        return response.split("AI: ")[1].split("Subjects:")[0]
    except IndexError:
        return ""


def parse_subjects_from_response(response: str):
    try:
        return response.split("Subjects: |")[1].split("|")[:-1]
    except IndexError:
        return []


def repl():
    repl_commands = WordCompleter(['show_prompt', 'restart'], ignore_case=True)
    conversation = Conversation(searchEnginePrompt)
    while True:
        try:
            user_input = prompt('>>>',
                                history=FileHistory('history.txt'),
                                auto_suggest=AutoSuggestFromHistory(),
                                completer=repl_commands,
                                )
        except KeyboardInterrupt:
            sys.exit(0)

        if user_input == "show_prompt":
            print(conversation.conversation)
            continue
        if user_input == "restart":
            conversation = Conversation(searchEnginePrompt)
            continue

        (conversation, next_prompt) = conversation.get_next_prompt(user_input)
        response = get_response(next_prompt).choices[0].text
        conversation = conversation.add_response(response)
        print(response.split("AI: ")[1].split("Subjects:")[0])
        subjects = parse_subjects_from_response(response)
        search_links = [f"https://www.google.com/search?q={urllib.parse.quote_plus(subject)}" for subject in subjects]
        print("Subjects:", subjects)
        print("Search Links:", search_links)


if __name__ == "__main__":
    repl()

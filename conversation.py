class Conversation:
    def __init__(self, init_prompt: str):
        self.conversation = init_prompt

    def get_next_prompt(self, user_input: str):
        self.conversation += user_input
        return self, self.conversation

    def add_response(self, response: str):
        self.conversation += response + "\nHuman: "
        return self

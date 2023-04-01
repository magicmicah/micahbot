import logging

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.messages = []
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"User ID: {self.id} | User Name: {self.name} created.")
    
    def append_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_messages(self):
        return self.messages
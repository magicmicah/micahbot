import logging
import utils

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.messages = []
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"User ID: {self.id} - User Name: {self.name} created.")
        self.token_limit = 4000
        self.token_total = 0
    
    def append_message(self, role, content):
        token_length = utils.num_tokens_from_messages(self.messages)
        self.token_total = self.token_total + token_length
        while (token_length > self.token_limit):
            for item in self.messages:
                if item['role'] != 'system':
                    self.messages.remove(item)
            token_length = utils.num_tokens_from_messages(self.messages)

        self.messages.append({"role": role, "content": content})

    def get_messages(self):
        return self.messages
    
    def remove_message(self, role, content):
        for message in self.messages:
            if message["role"] == role and message["content"] == content:
                self.messages.remove(message)
                self.logger.info(f"User ID: {self.id} - User Name: {self.name} - Message: {message} removed.")
                return True
        return False
    
class UserRegistry:
    def __init__(self):
        self.registry = {}
        self.logger = logging.getLogger(__name__)
        self.logger.info("UserRegistry created.")

    def is_user_in_registry(self, id):
        if id in self.registry:
            return True
        else:
            return False

    def add_user(self, id, name):
        new_user = User(id, name)
        new_user.append_message("system", "Your name is Micahbot. Your purpose is to do the needful. ")
        self.registry[id] = new_user
        self.logger.info(f"User ID: {new_user.id} - User Name: {new_user.name} added to registry.")
    
    def remove_user(self, id):
        if id in self.user_data:
            del self.registry[id]
            self.logger.info(f"User ID: {id} removed from registry.")
    
    def display_all_users(self):
        for id, name in self.registry.items():
            self.logger.info(f"User ID: {id} - User Name: {name}")

    def get_user_messages(self, id):
        if id in self.registry:
            #self.logger.info(f"get_user_messages: User ID: {id} - User Name: {self.registry[id]} - User Messages: {self.registry[id].get_messages()}")
            return self.registry[id].get_messages()

    def append_user_message(self, id, role, content):
        if id in self.registry:
            self.registry[id].append_message(role, content)
            #self.logger.info(f"append_user_messages: User ID: {id} - User Name: {self.registry[id].get_messages()} - User Messages: {self.registry[id].get_messages()}")
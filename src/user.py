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
        new_user.append_message("system", "You are a chatbot. You are here to help people.")
        self.registry[id] = new_user
        self.logger.info(f"User ID: {new_user.id} | User Name: {new_user.name} added to registry.")
    
    def remove_user(self, id):
        if id in self.user_data:
            del self.registry[id]
            self.logger.info(f"User ID: {id} removed from registry.")
    
    def display_all_users(self):
        for id, name in self.registry.items():
            self.logger.info(f"User ID: {id} | User Name: {name}")

    def get_user_messages(self, id):
        if id in self.registry:
            # self.logger.info(f"User ID: {id} | User Name: {self.registry[id]} | User Messages: {self.registry[id].get_messages()}")
            return self.registry[id].get_messages()

    def append_user_message(self, id, role, content):
        if id in self.registry:
            self.registry[id].append_message(role, content)
            #self.logger.info(f"User ID: {id} | User Name: {self.registry[id].get_messages()} | User Messages: {self.registry[id].get_messages()}")
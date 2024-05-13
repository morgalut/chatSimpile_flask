# backend/chat/models.py

# Define your data models here
# For example, you can create a model for chat messages
class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def to_dict(self):
        return {'sender': self.sender, 'content': self.content}

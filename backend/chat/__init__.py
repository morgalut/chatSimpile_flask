# backend/chat/__init__.py

from flask import Blueprint

# Create a Flask Blueprint for the chat module
chat_blueprint = Blueprint('chat', __name__)

# Import routes and sockets
from backend.chat import routes, sockets

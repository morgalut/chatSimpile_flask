# backend\chat\routes.py
import os
from flask import Blueprint, jsonify, request

chat_blueprint = Blueprint('chat', __name__)

# List to store messages
messages = []

@chat_blueprint.route('/send_message', methods=['POST'])
def send_message():
    global messages
    data = request.json
    message = data.get('message')  # Extract the message from the request data
    messages.append(message)  # Add the message to the list of messages
    return jsonify({'message': 'Message sent successfully'})

@chat_blueprint.route('/get_messages', methods=['GET'])
def get_messages():
    global messages
    return jsonify({'messages': messages})

@chat_blueprint.route('/')
def index():
    return 'Hello, World!'

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app)  # Enable CORS for all routes
socketio = SocketIO(app)

from backend.chat.routes import chat_blueprint
app.register_blueprint(chat_blueprint)

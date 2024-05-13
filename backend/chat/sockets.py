# backend/chat/sockets.py

from backend import socketio

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    # Handle message logic here
    # You can emit messages back to clients using socketio.emit()

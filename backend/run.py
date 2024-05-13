# backend/run.py

import sys
sys.path.append('C:/Users/Mor/Desktop/curss2/p6/sociket_flask')  # Adjust the path accordingly

from backend import app, socketio

if __name__ == "__main__":
    socketio.run(app, debug=True)

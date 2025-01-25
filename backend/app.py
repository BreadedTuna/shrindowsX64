from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Backend is running!"

# WebSocket endpoint for streaming
@socketio.on('stream')
def handle_stream(data):
    emit('video', data, broadcast=True)

# WebSocket endpoint for input
@socketio.on('input')
def handle_input(data):
    print(f"Received input: {data}")
    emit('control', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

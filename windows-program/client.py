import cv2
import pyautogui
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
import websocket
import json

keyboard = KeyboardController()
mouse = MouseController()

# Stream screen
def stream_screen(ws):
    while True:
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode('.jpg', frame)
        ws.send(buffer.tobytes())

# Handle input
def on_message(ws, message):
    data = json.loads(message)
    if data['type'] == 'keydown':
        keyboard.press(data['key'])
        keyboard.release(data['key'])

# Connect WebSocket
ws = websocket.WebSocketApp(
    "ws://localhost:5000",
    on_message=on_message
)

ws.run_forever()

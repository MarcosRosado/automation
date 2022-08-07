import websocket
import threading

websocket.enableTrace(True)


def on_open(ws):
    ws.send("hi")


def on_message(ws, message):
    def run(*args):
        print(message)
        print("Message received...")

    threading.Thread(target=run).start()


def on_close(ws, close_status_code, close_msg):
    print(">>>>>>CLOSED")


if __name__ == "__main__":
    while True:
        wsapp = websocket.WebSocketApp("ws://localhost:3000", on_open=on_open, on_message=on_message, on_close=on_close)
        wsapp.run_forever()

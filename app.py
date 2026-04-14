from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8602858732:AAGV2AtJ-c3TdXQHBkrIH3fkPg96aGu0U-0"
CHAT_ID = "1531088804"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST', 'GET', 'OPTIONS'])
def webhook():
    if request.method == 'OPTIONS':
        return {"status": "ok"}

    data = request.json
    message = data.get("message", "No message")

    send_telegram(message)

    return {"status": "sent"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

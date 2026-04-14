
from flask import Flask, request
import requests
import os

app = Flask(__name__)

# =========================
# 🔐 YOUR CONFIG
# =========================
TOKEN = "8602858732:AAGV2AtJ-c3TdXQHBkrIH3fkPg96aGu0U-0"
CHAT_ID = "1531088804"

# =========================
# 🚀 SEND TELEGRAM MESSAGE
# =========================
def send_telegram(message):
    formatted = f"""
🚨 <b>LIVE SIGNAL</b>

{message}

━━━━━━━━━━━━━━━
📊 <b>APEX SNIPER PRO</b>
⚠️ Risk 1–2% per trade
━━━━━━━━━━━━━━━
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": formatted,
        "parse_mode": "HTML"
    }

    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Error:", e)

# =========================
# 🔥 WEBHOOK ROUTE
# =========================
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if data and "message" in data:
        send_telegram(data["message"])

    return "ok"

# =========================
# 🚀 START SERVER
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

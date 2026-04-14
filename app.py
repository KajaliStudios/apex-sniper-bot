from flask import Flask, request
import requests
from threading import Thread
import time

app = Flask(__name__)

TOKEN = "8602858732:AAGV2AtJ-c3TdXQHBkrIH3fkPg96aGu0U-0"
VIP_CHANNEL_ID = "-1003952526649"
FREE_GROUP_ID = "-1003955329099"

# =========================
# SEND TELEGRAM
# =========================
def send_telegram(chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print("Telegram error:", e)

# =========================
# BACKGROUND DELAY FUNCTION
# =========================
def send_free_delayed(msg):
    time.sleep(120)  # 2 min delay

    free_msg = f"""
📢 <b>FREE SIGNAL</b>

{msg}

⚠️ Upgrade to VIP for early entries
"""

    send_telegram(FREE_GROUP_ID, free_msg)

# =========================
# WEBHOOK
# =========================
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if data and "message" in data:
        msg = data["message"]

        # 🔴 VIP (instant)
        vip_msg = f"""
🚨 <b>VIP SIGNAL</b>

{msg}

━━━━━━━━━━━━━━━
📊 APEX SNIPER PRO
━━━━━━━━━━━━━━━
"""
        send_telegram(VIP_CHANNEL_ID, vip_msg)

        # 🟢 FREE (background delay)
        Thread(target=send_free_delayed, args=(msg,)).start()

    return "ok"

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

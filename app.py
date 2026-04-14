from flask import Flask, request
import requests

app = Flask(__name__)

# =========================
# 🔐 CONFIG
# =========================
TOKEN = "8602858732:AAGV2AtJ-c3TdXQHBkrIH3fkPg96aGu0U-0"

# 👉 ADD BOTH HERE
FREE_GROUP_ID = "-1003952526649"
VIP_CHANNEL_ID = "-1003952526649"

# =========================
# 🚀 SEND FUNCTION
# =========================
def send_telegram(chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    requests.post(url, json=payload)

# =========================
# 🔥 WEBHOOK
# =========================
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if data and "message" in data:
        msg = data["message"]

        # 🔴 VIP gets full signal
        vip_msg = f"""
🚨 <b>VIP SIGNAL</b>

{msg}

━━━━━━━━━━━━━━━
📊 APEX SNIPER PRO
━━━━━━━━━━━━━━━
"""

        # 🟢 FREE gets simplified / delayed style
        free_msg = f"""
📢 <b>FREE SIGNAL</b>

{msg}

⚠️ Upgrade to VIP for real-time entries
"""

        # SEND
        send_telegram(VIP_CHANNEL_ID, vip_msg)
        send_telegram(FREE_GROUP_ID, free_msg)

    return "ok"

# =========================
# 🚀 RUN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

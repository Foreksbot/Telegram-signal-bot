import os
from flask import Flask, request
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("7992107267:AAEnr1zJC_vITRbC-WjuV6llrLMIQ1FLPSs")     
TELEGRAM_CHAT_ID = os.getenv("7992107267")         

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{7992107267:AAEnr1zJC_vITRbC-WjuV6llrLMIQ1FLPSs}/sendMessage"
    payload = {
        "chat_id": 7992107267,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data and "message" in data:
        signal = data["message"]
        send_telegram_message(signal)
        return {"status": "success"}, 200
    return {"status": "error"}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

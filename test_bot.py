import os
import requests from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "✅ Bot is working! This is a test message."
}

response = requests.post(url, data=payload)
print(response.status_code, response.text)
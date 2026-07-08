import os
import requests
from dotenv import load_dotenv
from make_chart import create_chart

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_chart():
    chart_path = create_chart()

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(chart_path, "rb") as photo:
        files = {"photo": photo}
        data = {"chat_id": CHAT_ID, "caption": "📊 BTC/USDT — 🕐 1H candle closed"}
        response = requests.post(url, files=files, data=data)

    print(response.status_code, response.text)

if __name__ == "__main__":
    send_chart()
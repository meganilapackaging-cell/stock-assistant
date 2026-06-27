import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = """📈 Stock Assistant

✅ Hello! Your Stock Assistant is now working.

Next, I'll send:
• Top 4 52-week highs
• Top 4 52-week lows
• Market news
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print("Message sent!")

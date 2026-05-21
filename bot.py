import requests

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

updates = [
    "🚨 RRB: Latest railway updates check",
    "🚨 SSC: Latest SSC updates check"
]

for message in updates:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL_ID,
        "text": message
    }

    requests.post(url, data=data)

print("RRB + SSC workflow running")

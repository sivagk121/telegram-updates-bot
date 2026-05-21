import requests

BOT_TOKEN = "8686311310:AAHugfm5p7GBHXK-s_2RefiJQBFlpF-HZts"
CHANNEL_ID = "@sivagk121"

updates = [
    "🚨 RRB: Check latest notifications",
    "🚨 SSC: Check latest updates",
    "🚨 UPSC: New notification updates"
]

for message in updates:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL_ID,
        "text": message
    }

    response = requests.post(url, data=data)
    print(response.text)

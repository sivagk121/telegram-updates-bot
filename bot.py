1import requests
1/0
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
    requests.post(url, data=data)

print("NEW CODE RUNNING")

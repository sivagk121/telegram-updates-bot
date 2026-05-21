import requests

BOT_TOKEN = "8686311310:AAHugfm5p7GBHXK-s_2RefiJQBFlpF-HZts"
CHANNEL_ID = "@sivagk121"

message = "🚨 GitHub automation test"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHANNEL_ID,
    "text": message
}

requests.post(url, data=data)

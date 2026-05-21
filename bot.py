import requests
import os

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

updates = []

# RRB check
try:
    rrb = requests.get("https://www.rrbcdg.gov.in/").status_code
    if rrb == 200:
        updates.append("🚨 RRB: Website updated/check available")
except:
    pass

# SSC check
try:
    ssc = requests.get("https://ssc.gov.in/").status_code
    if ssc == 200:
        updates.append("🚨 SSC: Website updated/check available")
except:
    pass

# Send updates
for message in updates:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL_ID,
        "text": message
    }

    requests.post(url, data=data)

print("Done")


import requests
import os

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

updates = []

try:
    rrb = requests.get("https://www.rrbcdg.gov.in/").status_code
    if rrb == 200:
        updates.append("🚨 RRB update available")
except:
    pass

try:
    ssc = requests.get("https://ssc.gov.in/").status_code
    if ssc == 200:
        updates.append("🚨 SSC update available")
except:
    pass

new_update = "\n".join(updates)

# save previous update in GitHub file
LAST_FILE = "last_update.txt"

old = ""
if os.path.exists(LAST_FILE):
    with open(LAST_FILE,"r") as f:
        old = f.read()

if new_update != old and new_update != "":
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url,data={
        "chat_id": CHANNEL_ID,
        "text": new_update
    })

    with open(LAST_FILE,"w") as f:
        f.write(new_update)

print("Done")

import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

updates = []

try:
    rrb = requests.get("https://www.rrbcdg.gov.in/")
    soup = BeautifulSoup(rrb.text, "html.parser")
    title = soup.title.text

    updates.append(f"🚨 RRB Latest:\n{title}")

except:
    pass


try:
    ssc = requests.get("https://ssc.gov.in/")
    soup = BeautifulSoup(ssc.text, "html.parser")
    title = soup.title.text

    updates.append(f"🚨 SSC Latest:\n{title}")

except:
    pass


for msg in updates:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHANNEL_ID,
            "text": msg
        }
    )

print("Done")

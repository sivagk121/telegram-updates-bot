import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHANNEL_ID, "text": msg}
    )

try:
    page = requests.get("https://www.rrbcdg.gov.in/")
    soup = BeautifulSoup(page.text, "html.parser")

    links = soup.find_all("a")

    count = 0

    
for l in links:
    text = l.get_text(strip=True)
    href = l.get("href")

    if text and href and len(text) > 10:

        send(
f"""🚨 Chandigarh Test

{text}

🔗 {href}
"""
)

        count += 1

    if count == 15:
        break

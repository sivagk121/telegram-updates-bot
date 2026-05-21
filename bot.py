import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHANNEL_ID,
            "text": msg
        }
    )

URL = "https://rrbajmer.gov.in/Results"

try:
    page = requests.get(URL, timeout=20)
    soup = BeautifulSoup(page.text, "html.parser")

    links = soup.find_all("a")

    count = 0

    for l in links:

        text = l.get_text(" ", strip=True)
        href = l.get("href")

        if not text or not href:
            continue

        low = text.lower()

        if any(x in low for x in [
            "result",
            "cutoff",
            "cut off",
            "score",
            "answer",
            "technician",
            "alp",
            "je",
            "ntpc",
            "cen"
        ]):

            if not href.startswith("http"):
                href = "https://rrbajmer.gov.in/" + href.lstrip("/")

            send(
f"""🚨 RRB Ajmer Update

{text}

📄 {href}
"""
            )

            count +=1

        if count == 10:
            break

except Exception as e:
    send(str(e))

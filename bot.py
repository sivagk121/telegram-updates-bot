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

try:
    page = requests.get("https://www.rrbcdg.gov.in/")
    soup = BeautifulSoup(page.text, "html.parser")

    links = soup.find_all("a")

    keywords = [
        "result",
        "notification",
        "notice",
        "answer",
        "key",
        "alp",
        "ntpc",
        "je",
        "technician",
        "recruitment",
        "corrigendum"
    ]

    count = 0

    for l in links:
        text = l.get_text(strip=True)
        href = l.get("href")

        if (
            text
            and href
            and any(k in text.lower() for k in keywords)
        ):

            send(
f"""🚨 RRB Update

{text}

🔗 {href}
"""
            )

            count += 1

        if count == 10:
            break

except Exception as e:
    send(f"Error: {e}")

print("Done")

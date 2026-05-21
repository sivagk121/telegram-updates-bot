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

    rows = soup.get_text("\n", strip=True)

    keywords = [
        "Result",
        "Results",
        "Cut Off",
        "Technician",
        "ALP",
        "JE",
        "NTPC",
        "DV",
        "Written"
    ]

    found = []

    for k in keywords:
        if k.lower() in rows.lower():
            found.append(k)

    if found:

        send(
f"""🚨 RRB Ajmer

Detected:

{", ".join(found)}

🔗 {URL}
"""
        )

except Exception as e:
    send(str(e))

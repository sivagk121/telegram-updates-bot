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


URL = "https://www.rrbcdg.gov.in/employment-notices.php"

try:
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,"html.parser")

    links = soup.find_all("a")

    include = [
        "result",
        "answer",
        "notice",
        "notification",
        "exam",
        "score",
        "admit",
        "cen",
        "alp",
        "ntpc",
        "je",
        "technician"
    ]

    exclude = [
        "skip",
        "font",
        "social",
        "accessibility",
        "india",
        "railway colony",
        "office",
        "station",
        "maps",
        "candidate",
        "login"
    ]


    count = 0

    for l in links:

        text = l.get_text(" ",strip=True)
        href = l.get("href")

        if not text or not href:
            continue

        low = text.lower()

        if (
            any(x in low for x in include)
            and not any(y in low for y in exclude)
        ):

            if not href.startswith("http"):
                href = "https://www.rrbcdg.gov.in/" + href.lstrip("/")

            send(
f"""🚨 RRB Alert

{text}

🔗 {href}
"""
            )

            count +=1

        if count == 10:
            break


except Exception as e:
    send(str(e))

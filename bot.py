import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHANNEL_ID,"text": msg}
    )


# Chandigarh
try:
    url="https://www.rrbcdg.gov.in/"
    page=requests.get(url)

    soup=BeautifulSoup(page.text,"html.parser")

    links=soup.find_all("a")

    for l in links[:20]:

        text=l.get_text(strip=True)
        href=l.get("href")

        if text and href:

            if any(k in text.lower() for k in [
                "result",
                "notification",
                "answer",
                "alp",
                "je",
                "ntpc",
                "recruitment"
            ]):

                send(
f"""🚨 RRB Chandigarh

{text}

🔗 {href}
"""
)

except:
    pass


# SSC
try:
    page=requests.get("https://ssc.gov.in/")
    soup=BeautifulSoup(page.text,"html.parser")

    links=soup.find_all("a")

    for l in links[:20]:

        text=l.get_text(strip=True)
        href=l.get("href")

        if text and href:

            if any(k in text.lower() for k in [
                "result",
                "notification",
                "answer",
                "gd",
                "cgl",
                "chsl"
            ]):

                send(
f"""🚨 SSC

{text}

🔗 {href}
"""
)

except:
    pass

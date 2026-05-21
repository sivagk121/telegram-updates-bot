import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHANNEL_ID, "text": msg}
    )


URLS = [
("RRB Chandigarh","https://www.rrbcdg.gov.in/employment-notices.php"),
("SSC","https://ssc.gov.in/")
]

KEYWORDS = [
"result",
"answer key",
"notification",
"notice",
"exam date",
"admit card",
"score card",
"corrigendum",
"pdf"
]

for name,url in URLS:

    try:
        page=requests.get(url,timeout=10)
        soup=BeautifulSoup(page.text,"html.parser")

        links=soup.find_all("a")

        for l in links:

            text=l.get_text(" ",strip=True)
            href=l.get("href")

            if not text or not href:
                continue

            low=text.lower()

            if any(k in low for k in KEYWORDS):

                if not href.startswith("http"):
                    href=url+"/"+href

                send(
f"""🚨 {name}

{text}

🔗 {href}
"""
                )

    except:
        pass

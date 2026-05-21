import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

RRB_SITES = {
"Secunderabad":"https://rrbsecunderabad.gov.in/",
"Chennai":"https://www.rrbchennai.gov.in/",
"Bangalore":"https://www.rrbbnc.gov.in/"
}

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHANNEL_ID,
            "text": msg
        }
    )

for board,url in RRB_SITES.items():

    try:
        page=requests.get(url,timeout=10)
        soup=BeautifulSoup(page.text,"html.parser")

        links=soup.find_all("a")

        count=0

        for l in links:

            text=l.get_text(" ",strip=True)
            href=l.get("href")

            if text and href and len(text)>10:

                if not href.startswith("http"):
                    href=url+href

                send(
f"""🚨 {board} Test

{text}

🔗 {href}
"""
                )

                count +=1

            if count==5:
                break

    except Exception as e:
        send(f"{board} Error:\n{e}")

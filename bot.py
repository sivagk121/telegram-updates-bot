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


include = [
    "result",
    "results",
    "answer",
    "notification",
    "admit",
    "exam",
    "score",
    "cen",
    "alp",
    "ntpc",
    "je",
    "technician",
    "group d",
    "paramedical"
]

exclude = [
    "login",
    "candidate",
    "skip",
    "font",
    "social",
    "accessibility",
    "fraud",
    "helpline",
    "office"
]


for board,url in RRB_SITES.items():

    try:

        page=requests.get(
            url,
            timeout=10
        )

        soup=BeautifulSoup(
            page.text,
            "html.parser"
        )

        links=soup.find_all("a")

        count=0

        for l in links:

            text=l.get_text(
                " ",
                strip=True
            )

            href=l.get("href")

            if not text or not href:
                continue


            low=text.lower()

            if (
                any(
                    x in low
                    for x in include
                )

                and

                not any(
                    y in low
                    for y in exclude
                )
            ):

                if not href.startswith(
                    "http"
                ):

                    href=url+href


                send(
f"""🚨 {board} RRB

{text}

🔗 {href}
"""
                )

                count +=1


            if count==8:
                break


    except:
        pass

import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8686311310:AAHAALy0hOh-2dp98wo4rQFVmcw-taEd7NM"
CHANNEL_ID = "@sivagk121"

RRB_SITES = {
"Ahmedabad":"https://www.rrbahmedabad.gov.in/",
"Ajmer":"https://rrbajmer.gov.in/",
"Bangalore":"https://www.rrbbnc.gov.in/",
"Chandigarh":"https://www.rrbcdg.gov.in/",
"Chennai":"https://www.rrbchennai.gov.in/",
"Guwahati":"https://www.rrbguwahati.gov.in/",
"Kolkata":"https://rrbkolkata.gov.in/",
"Mumbai":"https://rrbmumbai.gov.in/",
"Patna":"https://rrbpatna.gov.in/",
"Secunderabad":"https://rrbsecunderabad.gov.in/"
}

for name,url in RRB_SITES.items():
    try:
        r = requests.get(url,timeout=10)
        soup = BeautifulSoup(r.text,"html.parser")

        title = soup.title.text[:80]

        msg=f"🚨 {name} RRB:\n{title}"

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id":CHANNEL_ID,
                "text":msg
            }
        )

    except:
        pass


# SSC
try:
    s=requests.get("https://ssc.gov.in/")
    soup=BeautifulSoup(s.text,"html.parser")

    title=soup.title.text

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id":CHANNEL_ID,
            "text":"🚨 SSC:\n"+title
        }
    )

except:
    pass

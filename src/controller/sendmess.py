from config import BOT_TOKEN
import requests

def sendmess(txt):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=-4181748266&text={txt}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}\n{response.text}")
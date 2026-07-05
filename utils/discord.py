import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("DISCORD_WEBHOOK")


def send_message(title, description):
    embed = {
        "title": title,
        "description": description,
        "color": 3447003
    }

    data = {
        "embeds": [embed]
    }

    response = requests.post(WEBHOOK, json=data)

    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(response.status_code)
        print(response.text)
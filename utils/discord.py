import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("DISCORD_WEBHOOK")


def send_embed(title, description, color=3447003):

    embed = {
        "title": title,
        "description": description,
        "color": color,
        "footer": {
            "text": "AI Intelligence System"
        },
        "timestamp": None
    }

    payload = {
        "embeds": [embed]
    }

    response = requests.post(
        WEBHOOK,
        json=payload,
        timeout=20
    )

    if response.status_code == 204:
        print("Discord message sent.")
    else:
        print(response.text)
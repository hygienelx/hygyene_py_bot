import pymsteams
import random
from consts import DAILY_HOOK_URL

def send():
    message = pymsteams.connectorcard(DAILY_HOOK_URL)

    color = random.randbytes(3).hex()
    message.color(color)

    message.title("Orden - Daily")
    message.text(get_text())

    message.send()

def get_text():
    team_members = ["Juanfa", "Clau", "Alex", "Santi", "Tomi"]
    random.shuffle(team_members)

    text_list = [ f"{i+1}) {m}" for i, m in enumerate(team_members)]
    return "\n".join(text_list)


import pymsteams
import random

def send_daily_message(hook_url):
    message = pymsteams.connectorcard(hook_url)

    color = random.randbytes(3).hex()
    message.color(color)

    message.title("Orden - Daily")
    message.text(get_text())

    message.send()

def get_text():
    team_members = ["Anto", "Clau", "Alex", "Santi", "Tomi", "Emi", "Juangui"]
    random.shuffle(team_members)

    text_list = [ f"{i+1}) {m}" for i, m in enumerate(team_members)]
    return "\n".join(text_list)


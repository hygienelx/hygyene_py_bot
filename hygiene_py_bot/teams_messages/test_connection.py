import pymsteams
from consts import DAILY_HOOK_URL

def send():
    message = pymsteams.connectorcard(DAILY_HOOK_URL)
    message.title("Message sent from python")
    message.text("Text")
    message.send()
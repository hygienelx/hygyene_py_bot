import schedule
import time
from dotenv import load_dotenv
from teams_messages import *
import os

load_dotenv()

DAILY_HOOK_URL = os.environ.get("DAILY_HOOK_URL")
QUARTER_TO_NINE = "11:45"

schedule.every().monday.at(QUARTER_TO_NINE).do(lambda: send_daily_message(DAILY_HOOK_URL))
schedule.every().tuesday.at(QUARTER_TO_NINE).do(lambda: send_daily_message(DAILY_HOOK_URL))
schedule.every().wednesday.at(QUARTER_TO_NINE).do(lambda: send_daily_message(DAILY_HOOK_URL))
schedule.every().thursday.at(QUARTER_TO_NINE).do(lambda: send_daily_message(DAILY_HOOK_URL))
schedule.every().friday.at(QUARTER_TO_NINE).do(lambda: send_daily_message(DAILY_HOOK_URL))

while True:
    schedule.run_pending()
    time.sleep(60)

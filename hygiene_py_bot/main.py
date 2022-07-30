import schedule
import time
from teams_messages import daily
from hygiene_py_bot.consts import QUARTER_TO_NINE

schedule.every().monday.at(QUARTER_TO_NINE).do(daily.send)
schedule.every().tuesday.at(QUARTER_TO_NINE).do(daily.send)
schedule.every().wednesday.at(QUARTER_TO_NINE).do(daily.send)
schedule.every().thursday.at(QUARTER_TO_NINE).do(daily.send)
schedule.every().friday.at(QUARTER_TO_NINE).do(daily.send)

schedule.every().sunday.at(QUARTER_TO_NINE).do(daily.send)

while True:
    schedule.run_pending()
    time.sleep(1)
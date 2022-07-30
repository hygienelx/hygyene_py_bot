import schedule
import time
from teams_messages import daily, test_connection

test_connection.send()

schedule.every().monday.at("08:45").do(daily.send)
schedule.every().tuesday.at("08:45").do(daily.send)
schedule.every().wednesday.at("08:45").do(daily.send)
schedule.every().thursday.at("08:45").do(daily.send)
schedule.every().friday.at("08:45").do(daily.send)

while True:
    schedule.run_pending()
    time.sleep(1)
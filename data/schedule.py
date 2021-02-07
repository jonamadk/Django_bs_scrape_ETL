# from datetime import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
# from data.scrape import *


# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(scrape_data, 'interval', seconds=5)
#     scheduler.start()


# import schedule 
# import time

# from data.scrape import *

# def job():
#     schedule.every.seconds(4).do(scrape_data)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
import schedule
import time


def job():
	print('boom')

schedule.every().day.at('08:16').do(job)

while True:
	schedule.run_pending()
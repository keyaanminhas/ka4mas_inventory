from datetime import datetime
from datetime import date

def get_time():
	while True:
		today = date.today()
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		current_date = today.strftime("%d/%m/%Y")
		if current_time == '13:04:30' and current_date == '13/01/2022':
			print(current_time, current_date)
			break

get_time()
from datetime import date, datetime

today = date.today()
todays_date = today.strftime("%d/%m/%Y")
print(todays_date)
print(datetime.now().strftime("%H:%M:%S"))
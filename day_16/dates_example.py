from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day,month,year,hour,minute)
print('timestamp',timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

new_year = datetime(2026,1,1)
print(new_year)

day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
print(day,month,year,hour,minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')


current_time = datetime.now()
t = current_time.strftime("%H:%M:%S")
print("Time:",t)

time_one = current_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Time one:",time_one)

time_two = current_time.strftime("%d/%m/%y, %H:%M:%S")
print("Time two:",time_two)

# 12. Python Date and Time Exercise with Solutions

# Exercise 1: Print current date and time in Python
import datetime

# for date and time
print(datetime.datetime.now())
# for time only
print(datetime.datetime.now().time())

# Exercise 2: Convert string into a datetime object
from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
date_time_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(date_time_obj)

# Exercise 3: Subtract a week (7 days) from a given date in Python
given_date = datetime(2020, 2, 25)
from datetime import datetime, timedelta

print(given_date)
days_to_substract = 7
res_date = given_date - timedelta(days_to_substract)
print(res_date)

# Exercise 4: Print a date in a the following format
from datetime import datetime

given_date = datetime(2020, 2, 25)
print(given_date.strftime("%A %d %b %Y"))

# Exercise 5: Find the day of the week of a given date
given_date = datetime(2020, 7, 26)
print(given_date.strftime("%A"))

# Exercise 6: Add a week (7 days) and 12 hours to a given date
given_date = datetime(2020, 3, 22, 10, 0, 0)
days_to_add = 7
res_date = given_date + timedelta(days=days_to_add, hours=12)
print("new date will be: \n", res_date)

# Exercise 7: Print current time in milliseconds
import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)

# Exercise 8: Convert the following datetime into a string
given_date = datetime(2020, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)

# Exercise 9: Calculate the date 4 months from the current date
from dateutil.relativedelta import relativedelta

given_date = datetime(2020, 2, 25).date()
months_to_add = 4
result_date = given_date + relativedelta(months=+ months_to_add)
print(result_date)

# Exercise 10: Calculate number of days between two given dates
date_1 = datetime(2020, 2, 25).date()
date_2 = datetime(2020, 9, 17).date()
delta = None
if date_1 > date_2:
    delta = date_1 - date_2
else:
    delta = date_2 - date_1

print("Difference of the days will be: \n", delta.days)

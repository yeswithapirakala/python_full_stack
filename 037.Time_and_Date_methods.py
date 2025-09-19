#Date Methods
import datetime
import time

from datetime import date

today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

#time methods
from datetime import datetime

now = datetime.now()
print("Now:", now)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

#Also using time module:
print("Current Time (epoch):", time.time())
print("Local Time:", time.ctime())
time.sleep(2)   # wait 2 seconds
print("After 2 seconds")
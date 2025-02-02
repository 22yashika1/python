#Write a Python program to calculate the number of days between two dates.
from datetime import date
f_date = date(2001,5,8)
l_date = date(2025,5,9)
delta= l_date-f_date
print(delta.days)

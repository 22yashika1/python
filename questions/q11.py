#Write a Python program to display the current date and time.
import datetime
now= datetime.datetime.now()
print ("Current date and time : ")
print(now.strftime("%d/%m/%Y, %H:%M:%S"))
#the strftime() method of the datetime object to format the date and time as a string in the format "YYYY-MM-DD HH:MM:SS" and prints it to the console.
#Write a Python program that calculates the area of a circle based on the radius entered by the user.
from math import pi                #pi constant from the math mudule
radius = float(input("enter your radius value : "))
area = pi * radius **2 
print("The area of the circle with radius " + str(radius) + " is: " + str(area))

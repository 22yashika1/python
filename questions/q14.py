#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
values = input("Enter your values separated with commas please : ")
list = values.split(",")
tuple = tuple(list)
print(list , tuple)
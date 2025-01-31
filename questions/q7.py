#Calculate the multiplication and sum of two numbers
#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
number1 = int(input("enter your first number: "))
number2 = int(input("enter your second number: "))
product = number1*number2
if product <= 1000:
    print (product)
else:
    print (number1+number2)
    
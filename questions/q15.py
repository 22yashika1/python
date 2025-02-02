#Write a Python program that accepts a filename from the user and prints the extension of the file.
filename = input("Enter your file name : ")
file_extension = filename.split(".")
print("The file extension of the file is :" + repr(file_extension[-1]))
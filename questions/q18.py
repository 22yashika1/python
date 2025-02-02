#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
x = int(input("enter your value : "))
n1= int('%s' % x)                           # Convert 'x' to an integer
n2 = int ('%s%s' % (x,x))                   # Concatenate 'x' with itself and convert to an integer
n3= int('%s%s%s' % (x,x,x))
print(n1+n2+n3)
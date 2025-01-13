#program to print natural numbers
number = int(input("enter you natural no. :"))
for j in range (1,number+1):
    a=[ ]
    for i in range (1, j+1):
        print (i, sep=" " , end= " ")
        
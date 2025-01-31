#Print the Sum of a Current Number and a Previous number.
previous_number = 0
for i in range(1,11):
    sum=previous_number + i 
    print ("current number" , i , "previous num" , previous_number , "final" , sum)
    previous_number = i 
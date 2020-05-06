#Number of digits in a number
n=int(input("Enter a number= "))
count=0
while(n>0):
    count=count+1
    n=n//10
total=count    
print("The number of digits in the number is =  ",total)
    
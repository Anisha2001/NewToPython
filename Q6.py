#Fibonacci series
fibbo=[]
n=int(input("Enter a number = "))
l=int(input("Enter length of fibbonacci series = "))
a=0
b=1
fibbo.append(a)
fibbo.append(b)
s=0
while (s<=l):
    s=a+b
    a=b
    b=s
    if (s<=l):
        fibbo.append(s)
 
if(s==n):
    print(f'{n} is a fibonacci series element')
else:
    print(f'{n} is not a fibonacci series element')
print("Fibonacci series ")
print(fibbo)
    
       
    
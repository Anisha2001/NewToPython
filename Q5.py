#
prime=[]
n=int(input("Enter a number = "))
l=100
i=1
while i<=l:
    c=0
    j=1
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        prime.append(i)
    i+=1
if (i-1)==l:
    if (c==2):
        print("Input number is prime")
    else:
        print("Input number is not prime")
print("List of prime numbers ")
print(prime) 
       
    
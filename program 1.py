#multiplication_or_sum
def multiplication_or_sum(a,b):
    product=a*b
    if(product<=1000):
        return product
    else:
        return a+b
number1=int(input("Enter 1st number = "))
number2=int(input("Enter 2nd number = "))

result=multiplication_or_sum(number1,number2)
print("The result is = ",result)
1
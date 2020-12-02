#create function to display addition,subtraction,multiplication,division
def func(a,b):
    print("Addtion of",a,"and",b,"is",a+b)
    print("Subtraction of",a,"and",b,"is",a-b)
    print("Multiplication of",a,"and",b,"is",a*b)
    print("Division of",a,"and",b,"is",a//b)
n=int(input("Enter the two integer number:"))
n1=int(input())
func(n,n1)
print('\n')


#function covid
def covid(name,temp=98):
    print("Name:",name)
    print("Temperature:",temp)
n=input("Enter the name:")
n1=input("Enter the body temperature:")
covid(n,n1)

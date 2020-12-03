#add +2 to every value to element in list
n=int(input("Enter the length of the list:"))
print("Enter the element of the list:")
lst=[]
for i in range(0,n):
    a=int(input())
    lst.append(a)
print("Original List:")
print(lst)
for i in range(0,n):
    lst[i] +=2
print("After the change:")
print(lst)
print('\n')


#to get given pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
print('\n')


#fibonacci sequence
n=int(input("Enter the number for fibonacci series:"))
f=0
s=1
print("The fibonacci series:-")
print(f,end=' ')
for i in range(1,n):
    t=s
    s=s+f
    f=t
    print(t,end='  ')
print('\n')


#armstrong number
n=int(input("Enter the number to check the number is armstrong r not:"))
t=n
s=0
while t > 0:
    r =t % 10
    s+=  r ** 3
    t //= 10
if(n == s):
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")
print('\n')


#multiples of 9
n=int(input("Enter the base of multiples of 9:"))
print("Multiplication of 9:")
for i in range(1,n+1):
    print("9 *",i,"=",9*i)
print('\n')


#number is -ve r +ve
n=int(input("Enter the number:"))
if(n > 0):
    print(n,"is postive number")
else:
    print(n,"is negative number")
print('\n')


#convert number of days to age
n=int(input("Enter the number of days :"))
age= n//365
print("The age is",age)
print('\n')


#trigonomentry function
import math
n=int(input("Enter the degree:"))
val=math.radians(n)
print("Enter the function need to find trigonomentry(sin,cos,tan,asin,acos,atan,sinh,cosh,tanh):")
print("=>")
func=input()
if(func == "sin"):
    print("Sine of",n,"is",math.sin(val))
else:
    if(func =="cos"):
        print("Cosine of",n,"is",math.cos(val))
    else:
        if(func == "tan"):
            print("Tangent of",n,"is",math.tan(val))
        else:
            if(func == "asin"):
                print("Inverse of sine ",n,"is",math.asin(val))
            else:
                if(func =="acos"):
                    print("Cosine Inverse of",n,"is",math.acos(val))
                else:
                    if(func == "atan"):
                        print("Inverse of Tangent ",n,"is",math.atan(val))
                    else:
                        if(func == "sinh"):
                            print("Hyperbolic Sine of",n,"is",math.sinh(val))
                        else:
                            if(func =="cosh"):
                                print("Hyperbolic Cosine of",n,"is",math.cosh(val))
                            else:
                                if(func == "tanh"):
                                    print("Hyperbolic Tangent of",n,"is",math.tanh(val))
                                else:
                                    print("Error:Invalid fuction")
        print('\n')


        #Calculator
        a=int(input("Enter the two number:"))
        b=int(input())
        f=input("Enter the operation (+,-,*,/):")
        if(f == '+'):
            print("Addition of",a,"and",b,"is",a+b)
        else:
            if(f =='-'):
                print("Subtraction of",a,"and",b,"is",a-b)
            else:
                if(f == '*'):
                    print("Multiplication of",a,"and",b,"is",a*b)
                else:
                    if(f == '/'):
                        print("Division of",a,"and",b,"is",a/b)
                    else:
                        print("Error:Invalid Operation")

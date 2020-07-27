#!/usr/bin/env python
# coding: utf-8

# # Part-A
# 
# 
# # Implement User Interactive Calculator Using Python

# In[1]:


def add(a,b):      #function for addition
    return a+b
def sub(a,b):      #function for subtraction
    return a-b
def multiply(a,b):  #function for multiplication
    return a*b
def div(a,b):       #function for division
    return a/b
def dis(speed,time): #function for distance
    return speed*time
def speed(d,t):    #function for calculating speed
    return d/t
def intrest(p,t,r):   #function for claculating intrest
    return (p*t*r)/100
print("select any one choice")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.distance")
print("6.Speed")
print("7.Intrest")
choice=int(input())
while(choice<=7):
    if(choice==1):
        a=float(input("enter first number : "))
        b=float(input("enter second number : "))
        print(add(a,b))
    elif(choice==2):
        a=float(input("enter first number: "))
        b=float(input("enter second number : "))
        print(sub(a,b))
    elif(choice==3):
        a=float(input("enter first number : "))
        b=float(input("enter second number : "))
        print(multiply(a,b))
    elif(choice==4):
        a=float(input("enter first number : "))
        b=float(input("enter second number : "))
        print(div(a,b))
    elif(choice==5):  
        speed=float(input("enter speed in km/hr:"))
        time=float(input("enter time in hrs:"))
        print(dis(speed,time))#speed*time
    elif(choice==6):
        a=float(input("enter distance in km : "))
        b=int(input("enter time in hours : "))
        print(speed(a,b))
    elif(choice==7):
        p=float(input("enter pricipal amount : "))
        t=int(input("enter number of years : "))
        r=int(input("enter rate of intrest : "))
        print(intrest(p,t,r))
    break
if not choice<=7:
    print("invalid input")


# # Python Program to Calculate Area and Perimeter of Square,Rectangle,Rhombus,Parallelogram

# In[2]:


def area(a,b):
    print("area of square is ",a*a)
    print("area of rectangle is ",a*b)
    print("area of rhombus is ",(a*b)/2)
    print("area of paralellogram is ",end="")
    return a*b
def perimeter(a,b):
    print("perimeter of square is ",4*a)
    print("perimeter of rectangle is ",2*(a+b))
    print("perimeter of rhombus is ",4*a)
    print("perimeter of paralellogram is ",end="")
    return 2*(a+b)
a=int(input("enter a value : "))
b=int(input("enter b value : "))
print(area(a,b))
print(perimeter(a,b))


# # Part-B ;Python Program to Print cube Sum of first n natural Numbers.

# In[3]:


def cubesum(n):  #defining a function
    s=0          # initialising sum to 0
    for i in range(1,n+1):
        s=s+(i**3)   # calculating cube of each number and adding to sum
    return s
n=int(input("enter the value of n : "))   # reading the input from user
k=cubesum(n)
print("cube sum of n natural numbers is ",k)   # printing the result


# # Python Program to Check if a given String is Palindrome or Not.

# In[4]:


def isPalindrome(s): 
    return s == s[::-1] 

s = "abcba"
b="pravallika"
ans = isPalindrome(s) 
ans1 = isPalindrome(b)
if ans: 
    print("Yes") 
else: 
    print("No")
if ans1:
    print("yes")
else:
    print("No")


# In[ ]:





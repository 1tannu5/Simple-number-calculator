#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
print("\t___calculator___")


# In[ ]:


def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a > b:
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("\nThe quotient is: %s" %q)
    print("\nThe reminder is: %s" %r)
def sqr(a):
    x=math.sqrt(a)
    return x
while(True):
    print("\n\nChoose the operation you want to perform: ")
    print("\n\t1.Addition")
    print("\n\t2.Substract")
    print("\n\t3.Multiply")
    print("\n\t4.Division")
    print("\n\t5.Square root")
    print("\n\t6.Exit")
    
    choice = int(input('>'))
    if choice ==1:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        s= sum(num1,num2)
        print("the sum is: %s" %s)
    elif choice ==2:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        m= sub(num1,num2)
        print("the sum is: %s" %m)
    elif choice ==3:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        x= mul(num1,num2)
        print("the sum is: %s" %x)
    elif choice ==4:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        d= div(num1,num2)
        print("the sum is: %s" %d)
    elif choice ==5:
        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        sr= sqr(num1,num2)
        print("the sum is: %s" %sr)
    else:
        print("Exiting the calculator. Bye..")
        break


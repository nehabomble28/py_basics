#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:01:56 2020

@author: nehab28
"""
print("-------MENU FOR CALCULATOR-----------")
print("1. Addition of two numbers:")
print("2. Difference between two numbers:")
print("3. Product of two numbers:")
print("4. Quotient of divison between two numbers:")
print("5. Remainder of divison between two numbers:")
num = int(input("Enter your choice: "))

if num==1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition is " , (a+b))
elif num==2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Difference is ", (a-b))
elif num==3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Product is ", (a*b))
elif num==4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Quotient is ", (a/b))
elif num==5:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Remainder is ", (a%b))
else:
    print("Enter proper choice!")

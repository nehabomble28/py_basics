#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:26:28 2020

@author: nehab28
"""

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

if (num1>=num2)and(num1>=num3):
    largest = num1
elif (num2>=num1)and(num2>=num3):
    largest = num2
else:
    largest = num3
print("The largest number is ",largest)
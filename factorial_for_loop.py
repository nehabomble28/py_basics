#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:54:09 2020

@author: nehab28
"""

factorial  = 1

num = int(input("Enter the number: "))

if num<0:
    print("Sorry! factorial of negative number doesn't exist")
elif num==0:
    print("The factorial of 0 is 1" )
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial of %d is %d" %(num,factorial))

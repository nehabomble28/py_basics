#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:59:21 2020

@author: nehab28
"""

#Write a Program to find square root of a given number. Read number from user

num = int(input("Enter the number: "))

if num<0:
    print("Negative number's square root not possible.")
else:
    num_sqrt = num ** 0.5
    print("The squareroot of %d is %d" %(num, num_sqrt))

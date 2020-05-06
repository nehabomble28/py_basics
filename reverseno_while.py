#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:22:42 2020

@author: nehab28
"""

number = int(input("Enter the number to be reversed: "))
reverse = 0
while number>0:
    remainder = number%10
    reverse = (reverse*10)+remainder
    number = number//10
print("The reverse of the number is " , reverse)
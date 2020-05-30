#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:55:48 2020

@author: nehab28
"""
#Write a Python Program to swap two variables. Read numbers from user

num1 = int(input("Enter the first number:" ))
num2 = int(input("Enter the second number: "))

print("Before Swapping the numbers: num1 = %d and num2 = %d" %(num1,num2))
num1,num2 = num2,num1
print("After Swapping the numbers: num1 = %d and num2 = %d" %(num1,num2))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:13:43 2020

@author: nehab28
"""

def fibo(num):
    if num <= 1:
        return num
    else:
        return (fibo(num - 1) + fibo(num - 2))
    
num = int(input("Enter your limit to display fibonacci series: "))

if num <= 0:
    print("Please enter positive integer")
else:
    print("Fibonacci Series: ")
    for i in range(1,num):
        print(fibo(i))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:37:09 2020

@author: nehab28
"""

def addfun(num):
    return (num+10)

num = int(input("Enter the number to perform addition on: "))

sum = addfun(num)

print("\nThe Sum after adding 10 to the given number is ", sum)
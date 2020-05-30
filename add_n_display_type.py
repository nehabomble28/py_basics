#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:08:42 2020

@author: nehab28
"""

#Write a function to add n elements from user in list, display each element and type of each element
import collections

def addition(num):
    add = 0

    for n, count in list(num.items()):
        n = int(n)
        print("%d" %(n) , type(n))
        add = add + n
    return add

userInput = input("Enter the numbers to perform addition: \n\n")
userList = userInput.split()
numbers = []
num = collections.Counter(userList)
print("")

    
sum = addition(num)
print("The Addition of given numbers is ", sum)
    

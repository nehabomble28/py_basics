#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:51:17 2020

@author: nehab28
"""
#Write a python program to count the number of strings where the string length is 2 or more in the list of strings

count = 0

userList = input("Enter the list: ")
words = userList.split()
print("\n" , words , "\n")

for word in list(words):
    if (len(word) >= 2):
        print(word)
        count=count+1   
        
print("\nThe number of words with length as 2 or greater than 2 is: %d" %(count))

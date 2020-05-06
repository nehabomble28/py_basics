#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:12:50 2020

@author: nehab28
"""

lower=1
upper=200

print("Prime numbers between ",lower," and ",upper," are: ")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
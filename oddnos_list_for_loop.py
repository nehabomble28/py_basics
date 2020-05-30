#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:31:54 2020

@author: nehab28
"""
#Write code to create a list of odd numbers from 1 through 20 numbers and assign that list to the variableoddnums

oddnums = []
for i in range(1,20):
    if (i % 2!= 0):
        oddnums.append(i)
print("Odd Numbers List is: ", oddnums)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:32:29 2020

@author: nehab28
"""

#Session 1  Assignment 29/05/2020 Day2
#Write a python program to read first 10 characters from text file.

'''infile = open('data.txt' , 'r')

lines = ''

for line in infile:
    lines = line
infile.close()

print(lines[0:10])'''

with open('data.txt') as f:
    while True:
        c = f.read(10)
        if not c:
            print("End of File")
            break
        print("", c)
        break
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:57:35 2020

@author: nehab28
"""

lines = 0
words = 0
letters = 0

for line in open('data.txt'):
    lines = lines + 1
    letters = letters + len(line)
    
    pos = 'out'
    for letter in line:
        if (letter!= ' ' and pos == 'out'):
            words = words + 1
            pos = 'in'
        elif (letter == ' '):
            pos = 'out'

print("Lines: ", lines)
print("Words: ", words)
print("Characters: ", letters)
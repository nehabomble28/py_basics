#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:32:29 2020

@author: nehab28
"""

#Write a python program to read first 10 characters from text file.

with open('data.txt') as f:
    while True:
        c = f.read(10)
        if not c:
            print("End of File")
            break
        print("", c)
        break

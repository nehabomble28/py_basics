#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:44:54 2020

@author: nehab28
"""

outfile = open('write.txt' , 'w+')
string = 'Hello'
n = outfile.write(string)

if (n <= 0):
    print("Error!")
else:
    print("Writing to a file successful")

outfile.close()

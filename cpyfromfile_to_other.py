#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:54:40 2020

@author: nehab28
"""

infile = open('data.txt' , 'r')
lines = ''
for line in infile:
    lines = line
infile.close()

outfile = open('write.txt' , 'w+')
n = outfile.write(lines)
if (n <= 0):
    print("Error!")
else:
    print("Writing to a file successful")

outfile.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:41:53 2020

@author: nehab28
"""

def decision(input_str):
    if (len(input_str) > 20):
        return "This is a long string"
    elif (len(input_str) <= 20):
        return "This is a short string"
    else:
        return "This is a string"
    
input_str = input("Enter the string: ")
output_msg = decision(input_str)
print(output_msg)

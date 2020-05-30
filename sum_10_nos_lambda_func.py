#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:48:50 2020

@author: nehab28
"""
from functools import reduce

sequence = [1,2,3,4,5,6,7,8,9,10]

sum = reduce((lambda x,y:x+y) , sequence)

print(sum)


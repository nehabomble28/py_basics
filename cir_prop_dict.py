#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:13:01 2020

@author: nehab28
"""
#Create a dictionary of radius and circumference as key value paors, Use comprehension

properties = ['radius' , 'circumference']
prop_value = [25.00 , 157.08]

circle_dict = {}

for (key,value) in zip(properties,prop_value):
    circle_dict[key] = value
    
print("The dictionary of circle using comprehension is: " , circle_dict)

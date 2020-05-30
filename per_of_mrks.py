#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:03:18 2020

@author: nehab28
"""

#Write a program to accept marks of five subjects, calculate percentage and display on the screen

per = 0.0
total = 0.0

ds = float(input("Enter your marks in Data Structures: "))
cn = float(input("Enter your marks in Computer Networks: "))
os = float(input("Enter your marks in Operating Systems: "))
dbms = float(input("Enter your marks in Database Management System: "))
ml = float(input("Enter your marks in Machine learning: "))

total = 50 + 50 + 50 + 50 + 50

print("\n\nThe Result is as follows: ")
print("Data Structures = ", ds)
print("Computer Networks = ", cn)
print("Operating Systems = ", os)
print("Database Management System = ", dbms)
print("Machine Learning = ", ml)

per = (((ds + cn + os + dbms + ml)/total)*100)

print("\n Percentage = ", per)


















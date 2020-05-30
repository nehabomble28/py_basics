#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:08:09 2020

@author: nehab28
"""
#Session 1 Assignment 28/05/2020
#Write a python program to accept a list of five numbers and perform following operations:
# a) Find Minimum number b) Find Maximum number c) Reverse the list d) Sort the list

num = 5

userList = list(int(n) for n in input("Enter the list numbers or elements separated byy space: ").strip().split())[:num]
print("User List is ", userList)

print("Minimum number in the list is ", min(userList))
print("Maximum number in the list is ", max(userList))

sortList = userList
revList = userList

revList.reverse()
print("Reversed List: ", revList)

sortList.sort()
print("Sorted UserList: ", sortList)


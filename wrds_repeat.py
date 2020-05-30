#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:40:54 2020

@author: nehab28
"""

#Session 2 Assignment 28/05/2020
#Write a program to get text from user. Count how many times particular word occurred in the text

import collections

sentence = input("Enter the sentence to check the redundancy of each word: \n\n")
words = sentence.split()
word_counts = collections.Counter(words)
print("")
for word, count in sorted(word_counts.items()):
    print("%s is repeated %d time%s." %(word, count, "s" if count > 1 else ""))

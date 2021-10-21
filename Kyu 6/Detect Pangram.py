# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:33:33 2021

@author: martsc1
"""
import string
def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    pangram = True
    for letter in alphabet:
        if letter not in s.lower():
            pangram = False
            break
    return pangram
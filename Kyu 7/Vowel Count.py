# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:35:49 2021

@author: martsc1
"""
def get_count(sentence):
    vowels = ['a','e','i','o','u']
    nr = 0
    for letter in sentence:
        if letter in vowels:
            nr += 1
            
    return nr
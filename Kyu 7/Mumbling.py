# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:35:15 2021

@author: martsc1
"""
def accum(s):
    mumble = []
    count = 0
    for letter in s:
        mumble.append(letter.upper())
        if count != 0:
            mumble.append(count*letter.lower())
        mumble.append('-')
        count += 1
    mumble.pop(-1)
    return ''.join(mumble)
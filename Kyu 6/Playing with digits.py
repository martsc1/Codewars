# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:54:23 2021

@author: martsc1
"""
def dig_pow(n, p):
    nr = 0
    pow = p
    for digit in str(n):
        nr += int(digit)**pow
        pow += 1
    if nr % n == 0:
        return nr / n
    else:
        return -1




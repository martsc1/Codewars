# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:34:23 2021

@author: martsc1
"""
def digital_root(n):
    root = n
    while len(str(root)) > 1:
        counter = 0
        for digit in str(root):
            counter += int(digit)
        root = counter    
                
    return root
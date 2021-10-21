# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:32:38 2021

@author: martsc1
"""
def find_it(seq):
    for nr in seq:
        if seq.count(nr) % 2 == 1:
            return nr
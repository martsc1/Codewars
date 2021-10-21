# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:35:31 2021

@author: martsc1
"""
def DNA_strand(dna):
    output = []
    for letter in dna:
        if letter == 'A':
            output.append('T')
        elif letter == 'T':
            output.append('A')
        elif letter == 'C':
            output.append('G')
        elif letter == 'G':
            output.append('C')
         
    return ''.join(output)
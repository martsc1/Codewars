# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:33:51 2021

@author: martsc1
"""
def solution(number):
    treefives = []
    if number < 0: 
        return 0
    else:
        tree = int((number-1)/3)
        five = int((number-1)/5)
        for nr in range(five+1):
            treefives.append(nr*5)
        for nr in range(tree+1):
            if nr*3 not in treefives:
                treefives.append(nr*3)
        return sum(treefives)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:34:50 2021

@author: martsc1
"""
def create_phone_number(n):
    number = "(%s) %s-%s"%(''.join(map(str,n[0:3])), ''.join(map(str,n[3:6])),''.join(map(str,n[6:])))
    return number
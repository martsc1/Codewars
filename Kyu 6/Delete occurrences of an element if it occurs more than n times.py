# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:32:59 2021

@author: martsc1
"""
def delete_nth(order,max_e):
    for number in order:
        while order.count(number) > max_e:
            order.pop(max(index for index, item in enumerate(order) if item == number))
    return order
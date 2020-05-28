# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Easy

import math

def restaurant(l, b):
    req = math.gcd(l, b)
    print(req)
    val = (l*b)/(req**2)
    return int(val)
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        lb = input().split()
        l = int(lb[0])
        b = int(lb[1])

        result = restaurant(l, b)
        print(result)
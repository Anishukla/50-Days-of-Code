# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())

for i in range(T):
    N = int(input())
    val = 0
    j = 1
    while(N>0):
        if val>0:
            val = val*10 + N%10
        else: 
            val = val + (N%10)
        
        N = int(N/10)
        j=j+1
    print(val)
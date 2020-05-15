# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

import math

T = int(input())
for i in range(T):
    G = int(input())
    for j in range(G):
        A = list(map(int, input().split()))
        I = A[0]
        N = A[1]
        Q = A[2]
        if I==1:
            if Q==1:
                print(math.floor(N/2))
                
            else:
                print(math.ceil(N/2))
                
        elif I==2:
            if Q==2:
                print(math.floor(N/2))
                
            else:
                print(math.ceil(N/2))
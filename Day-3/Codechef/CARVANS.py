# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    c = 1
    for j in range(N-1):
        if A[j+1]>A[j]:
            A[j+1]=A[j]
            
        else:
            c=c+1
            
    print(c)
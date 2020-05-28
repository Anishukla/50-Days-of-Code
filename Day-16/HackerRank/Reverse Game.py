# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Easy

T = int(input())


for i in range(T):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    if (k < n-1-k):
        print(2*k+1)
    else:
        print(2*(n-1-k))
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level:Easy

t = int(input())
for k in range(t):
    n = int(input())
    L = [1, 2]
    i = 0
    while L[i]+L[i+1]<n:
        L.append(L[i]+L[i+1])
        i = i+1
        
    count = 0
    for i in range(len(L)):
        if L[i]%2 == 0:
            count = count+L[i]
    
    print(count)
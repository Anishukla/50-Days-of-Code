# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())

L = list(map(int, input().split()))

for i in range(T):
    L.append(L[i])
    
req = []
c = 0

for j in range(len(L)):
    if L[j]==1:
        c = c+1
        
    elif L[j]==0:
        req.append(c)
        c = 0
        
if len(req)==0:
    print(T)
        
else:
    print(max(req))
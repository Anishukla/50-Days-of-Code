# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

N, K = input().split()
N = int(N)
K = int(K)

A = list(map(int, input().split()))

L = []

for i in range(N):
    
    if A[i] not in L and len(L)<K:
        L.insert(0, A[i])
        
    if A[i] not in L and len(L)==K:
        L.pop()
        L.insert(0, A[i])
        
print(len(L))
print(*L)
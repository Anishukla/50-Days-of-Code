# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
import math

N, K = input().split()
N = int(N)
K = int(K)

A = list(map(int, input().split()))

val = 0
page = 1
count = 0

for i in range(N):
    req = math.ceil(A[i]/K)
    for j in range(req-1):
        La = []
        for q in range(1, K+1):
            La.append(j*K+q)
            
        if page in La:
            count = count+1
        page = page+1
        
    nxt = (req-1)*K
    La = []
    
    for p in range(nxt+1, A[i]+1):
        La.append(p)
    if page in La:
        count = count+1
    page = page+1
    
print(count)
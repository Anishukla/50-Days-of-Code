# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
from bisect import bisect_left,bisect_right


nxy = list(map(int, input().split()))
n = nxy[0]
x = nxy[1]
y = nxy[2]

L = []
for i in range(n):
    inout = list(map(int, input().split()))
    L.append(inout)
    
V = list(map(int, input().split()))

W = list(map(int, input().split()))

    
V = sorted(V)
W = sorted(W)

t = 1000000

for j in range(len(L)):
    i = L[j]
    if i[0] < V[0] or i[1] > W[-1]:
        continue
    
    l = bisect_left(V,i[0])
    u = bisect_right(W,i[1])
    
    if l >= len(V):
        l = len(V)-1
    elif V[l] > i[0]:
        l = l-1
    
    if u >= len(W):
        u = len(W)-1
    elif u != 0:
        if W[u-1]>=i[1]:
            u = u-1
        
    if (W[u]-V[l]+1)<t:
        t = (W[u]-V[l]+1)

print(t)
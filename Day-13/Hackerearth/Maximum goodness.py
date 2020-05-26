# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

# Write your code here

N = int(input())
A = list(map(int, input().split()))
L = [A[0]]
for i in range(1, len(A)):
    if A[i]==1 and L[i-1]<=0:
        L.append(1)

    elif A[i]==1:
        L.append(L[i-1]+1)

    elif A[i]==0:
        L.append(L[i-1]-1)
            
for i in range(len(L)):
    if L[i]<0:   
        L[i]=0
        
req = 0
res = 0
for i in range(len(L)):
    if L[i]==0 and L[i-1]==0:
        req = 0
    else:
        req=req+1
        
    if L[i]==max(L):
        res = req
        
print(res)
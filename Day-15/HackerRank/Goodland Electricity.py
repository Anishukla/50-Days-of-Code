# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Medium


n, k = input().split()
n = int(n)
k = int(k)
a=list(map(int,input().split()))

i, j, val, req, pos=0, 0, 0, 0, 0

while(i<n):
    val = val+1
    j = i+k-1
    if(j>n):
        j = n-1
    while (pos<=j<n and a[j]==0):
        j = j-1
    if(j<pos):
        print("-1")
        req=1
        break
    else:
        pos=j+1
        j = j+k
        i = j

if(req==0):      
    print(val)
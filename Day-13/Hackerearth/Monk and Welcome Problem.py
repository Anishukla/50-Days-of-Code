# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

# Write your code here
T = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = []
for i in range(T):
    res.append(A[i]+B[i])

print(*res)
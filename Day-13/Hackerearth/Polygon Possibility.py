# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

# Write your code here
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    val = sum(A)- A[N-1]
    if val>A[N-1]:
        print("Yes")

    else:
        print("No")
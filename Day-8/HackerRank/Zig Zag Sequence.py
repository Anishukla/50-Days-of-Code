# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

def findZigZagSequence(a, n):
    a.sort()
    mid = int(n/2)
    L = []
    for i in range(mid):
        L.append(a[i])

    for j in range(n-1, mid-1, -1):
        L.append(a[j])

    print(*L, end='')


test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

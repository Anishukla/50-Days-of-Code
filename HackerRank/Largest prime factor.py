# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

t = int(input())
for _ in range(t):
    n = int(input().strip())

    while (n%2==0):
        n = n//2

    if n==1:
        print(2)

    else:
        val = int(n**(1/2))
        i = 3
        while(i<=val):
            while (n%i==0):
                n = n//i
            if n!=1:
                i = i+2
            elif n==1:
                print(i)
                break
        if n>val:
            print(n)
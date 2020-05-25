#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:59:26 2020

@author: anishukla
"""
#Level: Medium

# Complete the stepPerms function below.
def stepPerms(n):
    A = [1, 2, 4]
    for i in range(3, n):
        A.append(A[i-3]+A[i-2]+A[i-1])

    return A[n-1]

if __name__ == '__main__':
    s = int(input())
    for s_itr in range(s):
        n = int(input())
        res = stepPerms(n)
        print(res)

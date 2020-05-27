# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Easy

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    A = sorted(A, reverse=True)
    B = sorted(B)

    for i in range(len(A)):
        if A[i]+B[i]<k:
            return "NO"

    return "YES"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        result = twoArrays(k, A, B)
        print(result)
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

# Complete the minimumSwaps function below.
def minimumSwaps(A, N):
    swap = 0
    i = 0
    while(i<N):
        if A[i]!=i+1:
            val = A[i]
            A[val-1], A[i] = A[i], A[val-1]
            swap = swap+1
        
        elif A[i]==(i+1):
            i = i+1 

    return swap
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = minimumSwaps(arr, n)
    print(res)
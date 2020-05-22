# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

# Complete the minimumBribes function below.
def minimumBribes(a, N):
    res = 0
    k = 0
    
    for i in range(N-1, -1,-1):
        
        if a[i]-(i+1)>2:
            k = k+1
            print("Too chaotic")
            break
        
        for j in range(max(0, a[i] - 2), i):
            if a[j]>a[i]:
                res=res+1
    if k==0:          
        print(res)

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q, n)
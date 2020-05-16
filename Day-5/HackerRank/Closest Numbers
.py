# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
# Level: Easy

# Complete the closestNumbers function below.
def closestNumbers(a):
    a = sorted(a)
    l = len(a)
    least = 20000000
    res = []
    for i in range(l-1):
        if a[i+1]-a[i]<least:
            least = a[i+1]-a[i]
            res = [a[i], a[i+1]]
        
        elif a[i+1]-a[i]==least: 
            res.append(a[i])
            res.append(a[i+1])

    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(result)
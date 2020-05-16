# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

# Complete the lilysHomework function below.
def lilysHomework(a):
    m = {}
    for i in range(len(a)):
        m[a[i]] = i 
        
    sorted_a = sorted(a)
    req = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            req = req+1
            
            temp = m[sorted_a[i]]
            m[a[i]] = m[sorted_a[i]]
            a[i], a[temp] = sorted_a[i], a[i]

    return req
        


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result1 = lilysHomework(list(arr))
    result2 = lilysHomework(list(reversed(arr)))
    result = min(result1, result2)
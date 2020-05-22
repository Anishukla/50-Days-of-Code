# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

# Complete the arrayManipulation function below.
def arrayManipulation(n, m, queries):
    Li = [0]*n
    for j in range(m):
        a = queries[j][0] - 1
        b = queries[j][1]
        c = queries[j][2]
        
        Li[a] = Li[a]+c

        if b<len(Li):
            Li[b] = Li[b]-c
        
    res = x = 0
    for i in Li:
        x=x+i
        if(res<x):
            res=x

    return res
    

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, m, queries)
    print(result)
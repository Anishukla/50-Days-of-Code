# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        val = a[0]
        a.remove(a[0])
        a.append(val)

    return a

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Medium

# Complete the solve function below.
Li  = [0]
val = 1
i=0

while val<=(10**10):
    Li.append(val)
    val = val + Li[i]
    i = i+1


def solve(n):
    if n in Li:
        return "IsFibo"

    else:
        return "IsNotFibo"


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())

        result = solve(n)
        print(result)

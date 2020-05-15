# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

def beautifulDays(i, j, k):
    c = 0
    for p in range(i, j+1):
        val = str(p)
        val2 = val[-1::-1]
        val2 = int(val2)
        res = abs(val2-p)
        if res%k == 0:
            c = c+1

    return c


if __name__ == '__main__':
    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])

    result = beautifulDays(i, j, k)
    print(result)
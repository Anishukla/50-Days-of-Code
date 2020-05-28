# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Easy


import math

def strangeGrid(r, c):
    a = math.ceil(r/2)
    count = 0
    if r%2==0:
        count = 1
    val = (a-1)*10 + count

    res = val + 2*(c-1)

    return res
    

if __name__ == '__main__':
    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])

    result = strangeGrid(r, c)
    print(result)
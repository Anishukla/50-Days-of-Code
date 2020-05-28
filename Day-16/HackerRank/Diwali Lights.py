# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Medium

def lights(n):
    res = (2**n)-1

    return res%(10**5)

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())

        result = lights(n)
        print(result)
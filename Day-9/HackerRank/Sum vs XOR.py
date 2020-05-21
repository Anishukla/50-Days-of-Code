# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

# Complete the sumXor function below.
def sumXor(n):
    if n>0:
        l=list(bin(n))[2:]
        c=l.count('0')
        return (2**c)

    elif n==0:
        return 1

if __name__ == '__main__':
    n = int(input().strip())
    result = sumXor(n)
    print(result)
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

# Complete the flippingBits function below.
def flippingBits(n):
    val = 2**32-1
    res = val-n

    return res

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        print(result)
    
#Method 2 
# Adding 1s complement of the number on 2**32
def flippingBits(n):
    return ~n + 2**32
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Easy

# Complete the twoArrays function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    count = 0
    val = 0

    for i in range(len(prices)):
        val = val + prices[i]
        if val<=k:
            count = count+1
        else:
            break
    
    return count


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().split()))

    result = maximumToys(prices, k)
    print(result)

# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        
        else:
            L = [True]*n

            for i in range(2, int(n**0.5)+1):
                if L[i]:
                    for j in range(i*i, n, i):
                            L[j]=False

            return len([x for x in L[2:] if x == True])
        
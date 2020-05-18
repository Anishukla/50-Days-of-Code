# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

class Solution:
    def isHappy(self, n: int) -> bool:
        req=n
        while req>9:
            req = 0
            req = 0
            while(n):
                req = req + (n%10)*(n%10)
                n = n//10
            n = req
            print(n)

        if req==1 or req==7:
            return True

        else:
            return False
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
# Level: Medium

class Solution:
    def findmsb(self, a:int) -> int:
        req = -1
        while a>0:
            a = a//2
            req = req+1
        return 2**req
        
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        while(m>0 and n>0):
            if m==n:
                res = res+m
                break
            msbm = self.findmsb(m)
            msbn = self.findmsb(n)
            if msbm != msbn:
                break
            
            res = res+msbm
                
            m = m-msbm
            n = n-msbm
            
        return res
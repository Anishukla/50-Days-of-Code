# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dis = {}
        for i, c in  enumerate(s):
            dis.setdefault(c, []).append(i)

        dit = {}
        for j, d in  enumerate(t):
            dit.setdefault(d, []).append(j)
            
        if len(dis)!=len(dit):
            return False
        
        else:
            for k in range(len(s)):
                if dis[s[k]]!=dit[t[k]]:
                    return False
                    break
            return True
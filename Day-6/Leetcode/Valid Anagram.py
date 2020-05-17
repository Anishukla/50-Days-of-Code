# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
# Level: Medium(O(n))

# Time Complexity:- O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        di = {}
        for i in range(len(s)):
            if s[i] not in di:
                di.update({s[i]:1})

            elif s[i] in di:
                di[s[i]] = di[s[i]]+1

        c=0
        for j in range(len(t)):
            if t[j] in di and di[t[j]]!=0:
                di[t[j]] = di[t[j]]-1

            elif t[j] not in di or di[t[j]]==0:
                return False
                break

        for k in di:
            if di[k]>0:
                return False
                break
            else:
                c = c+1
            
        if c==len(di):
            return True
        
        
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time Complexity:- O(nlog(n))
"""
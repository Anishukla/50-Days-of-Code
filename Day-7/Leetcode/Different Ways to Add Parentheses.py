# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        import operator
        
        OPS = {
            '*' : operator.mul,
            '-' : operator.sub,
            '+' : operator.add
        }
        
        results = []
        
        if not any(c in OPS for c in input):
            return [int(input)]
        
        for i, c in enumerate(input):
            if c in OPS:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                results += [OPS[c](int(l), int(r)) for l in left for r in right]
                        
        return results
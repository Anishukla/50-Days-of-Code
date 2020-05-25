# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Medium

# Complete the superDigit function below.
def superDigit(n, k):
    while int(n)>9:
        val = 0
        for i in range(len(n)):
            val = val+int(n[i])
        n = str(val)

    req = n*k
    while int(req)>9:
        valf = 0
        for i in range(len(req)):
            valf = valf+int(req[i])
        req = str(valf)

    return int(req)

if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])

    result = superDigit(n, k)
    
    print(result)

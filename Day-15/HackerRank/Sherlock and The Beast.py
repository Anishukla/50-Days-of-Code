# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Easy

# Complete the decentNumber function below.
def decentNumber(n):
    c_3 = 0
    val = n 
    x = 0
    while val%3 != 0:
        if val<3 and val!=0:
            print(-1)
            x = 1
            break

        val = val-5
        c_3 = c_3+5
        
    if x == 0:
        res = '5'*val+'3'*c_3
        print(res)

if __name__ == '__main__':
    t = int(input().strip())

    for i in range(t):
        n = int(input().strip())

        decentNumber(n)

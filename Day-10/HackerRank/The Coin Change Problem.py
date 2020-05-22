# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Medium

def getWays(n, c):
    # Write your code here
    table = [[0 for x in range(m)] for x in range(n+1)]     
    for i in range(m): 
        table[0][i] = 1
        
    for i in range(1, n+1): 
        for j in range(m): 
            x = table[i - c[j]][j] if i-c[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y 
              
    return table[n][m-1] 
    
            
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().split()))
    ways = getWays(n, c)
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

#Level: Medium

# Complete the solve function below.
def solve(dates):
    counts = [0]*100
    for i in range(n):
        req = dates[i]
        m = req[0]
        d = req[1]
        try:counts[int(str(d),m)]+=1
        except:pass

    return (sum(c*(c-1)//2 for c in counts))

if __name__ == '__main__':
    n = int(input())
    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = solve(dates)
    print(result)

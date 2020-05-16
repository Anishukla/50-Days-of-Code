# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
# Level: Easy

# Complete the marsExploration function below.
def marsExploration(s):
    val = len(s)//3
    count = 0
    for i in range(val):
        if s[3*i+0] != 'S':
            count = count+1

        if s[3*i+1] != 'O':
            count = count+1

        if s[3*i+2] != 'S':
            count = count+1

    return count


if __name__ == '__main__':
    s = input()
    res = marsExploration(s)
    print(res)

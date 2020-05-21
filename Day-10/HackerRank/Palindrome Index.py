# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Easy

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if s == s[::-1]:
        return (-1)
    else:
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s) - 1 - i]:
                return (i if ((s[:i] + s[i + 1:]) == (s[:i] + s[i + 1:])[::-1]) else len(s) - 1 - i)

        return -1
            

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)

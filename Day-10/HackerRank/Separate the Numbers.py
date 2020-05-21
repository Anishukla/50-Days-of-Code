# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
# Level: Easy

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s)==1:
        return 'NO'
    for i in range(1,len(s)//2+1):
        frst=prev=int(s[0:i])
        sub=s[0:i]
        while len(sub)+len(str(int(prev)+1))<=len(s):
            prev=int(prev)+1
            sub=sub+str(prev)
        if sub==s:
            return 'YES '+str(frst)
    return 'NO'

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        res = separateNumbers(s)
        print(res)

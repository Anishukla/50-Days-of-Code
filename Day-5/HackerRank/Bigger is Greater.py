# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
#Level: Medium

# Complete the biggerIsGreater function below.
def biggerIsGreater(s):
    for i in range(len(s)-1)[::-1]:
        if s[i] < s[i+1]:
            for j in range(i+1,len(s))[::-1]:
                if s[i] < s[j]:
                    lis = list(s) 
                    lis[i],lis[j]=lis[j],lis[i]
                    return "".join(lis[:i+1]+lis[i+1:][::-1])

    return 'no answer'
            

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        w = input()
        result = biggerIsGreater(w)

        print(result)
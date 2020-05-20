# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())
for i in range(T):
    n,m,k=map(int,input().split())
    di={}
    for i in range(k):
        r,c=map(int,input().split())
        di.update({(r,c):1})
    res=4*k 
    for i in di:
        r,c=i
        if (r,c-1) in di:
            res=res-1 
        if (r,c+1) in di:
            res=res-1         
        if (r+1,c) in di:
            res=res-1 
        if (r-1,c) in di:
            res=res-1 
    print(res)
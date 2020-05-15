# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())

for i in range(T):
    s = input()
    
    if len(s)%2==0:
        val = int(len(s)/2)
        a = s[:val]
        b = s[val:]
        
        for j in range(val):
            check = 0
            if a[j] not in b:
                print("NO")
                check = check+1
                break
            
            elif a[j] in b:
                b = b.replace(a[j], '', 1)
                
        if check==0:
            print("YES")
            
    if len(s)%2==1:
        val = int(len(s)/2)
        a = s[:val]
        b = s[val+1:]
        
        for j in range(val):
            check = 0
            if a[j] not in b:
                print("NO")
                check = check+1
                break
            
            elif a[j] in b:
                b = b.replace(a[j], '', 1)
                
        if check==0:
            print("YES")
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())
for i in range(T):
    G = input().split()
    act_c = int(G[0])
    req = G[1]
    res = 0
    
    for i in range(act_c):
        val = input().split()
        if val[0]=="CONTEST_WON":
            if int(val[1])<20:
                res = res+320-int(val[1])
                
            else:
                res = res+300
                
        
        elif val[0]=="TOP_CONTRIBUTOR":
            res = res+300
            
        elif val[0]=="BUG_FOUND":
            res = res+int(val[1])
            
        elif val[0]=="CONTEST_HOSTED":
            res = res+50
            
    if G[1]=="INDIAN":
        ans = res//200
        
    elif G[1]=="NON_INDIAN":
        ans = res//400
        
    print(ans)
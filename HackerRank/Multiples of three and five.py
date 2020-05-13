# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

T = int(input())
for i in range(T):
    N = int(input())
    
    c_three = (N-1)//3
    val_three = 3*c_three*(c_three+1)//2 
    
    c_five = (N-1)//5
    val_five= 5*c_five*(c_five+1)//2 
    
    c_15 = (N-1)//15
    val_15 = 15*c_15*(c_15+1)//2 
    
    print(val_three+val_five-val_15)
# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
n, m = map(int, input().split())
name = {}
nc = {}
ctr = {}
for _ in range(n):
    c_n, c_c = map(str, input().split())
    nc[c_n] = c_c
for _ in range(m):
    sub = input()
    if sub in name:
        name[sub] += 1
    else:
        name[sub] = 1
    if nc[sub] in ctr:
        ctr[nc[sub]] += 1
    else:
        ctr[nc[sub]] = 1
max_ctr = max(ctr.values())
chef = max(name.values())
ctr_list = []
chefl = []
for k,v in ctr.items():
    if v == max_ctr:
        ctr_list.append(k)
for k, v in name.items():
    if v == chef:
        chefl.append(k)

print(sorted(ctr_list)[0])
print(sorted(chefl)[0])
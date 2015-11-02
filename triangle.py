#!/bin/python3

import sys
import itertools

def getList(A):
    for x in itertools.combinations(A,3):
        if x[0] + x[1] > x[2]:
            yield list(x)
        else:
            continue

N = int(input().strip())
A = list(map(int,input().split()))
# your code goes here
#lis = [list(x) for x in itertools.combinations(A,3)]
gen = getList(A)
act, rt, obt = 0, 0, 0 
for l in gen:
    x,y,z = l[0]**2, l[1]**2, l[2]**2
    xny = x + y
    xyz = (x+y<z)
    if xny == z:
        rt += 1
    elif xyz:
        obt += 1
    else:
        act += 1
print("%d %d %d"%(act, rt, obt))


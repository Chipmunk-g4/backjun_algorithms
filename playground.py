# https://www.acmicpc.net/problem/2263

import sys
sys.setrecursionlimit(10**6)

V = int(input())
arb = list(map(int,input().split()))
abr = list(map(int,input().split()))

def rab(arbs, arbe, abrs, abre):
    r = abr[abre]
    print(r,end=' ')
    arbridx = arb.index(r)

    if arbs != arbridx:
        rab(arbs, arbridx-1, abrs, abrs + (arbridx-1-arbs))
    if arbe != arbridx:
        rab(arbridx+1, arbe, (abre-1)-(arbe-arbridx-1), abre-1)
rab(0,V-1,0,V-1)

"""
ABDCEFG
DBAECFG
DBEGFCA

7
4 2 1 5 3 6 7
4 2 5 7 6 3 1

1 2 4 3 5 6 7

1
2 | 3
4   5 | 6
        7

"""
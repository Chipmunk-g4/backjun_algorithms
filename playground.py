# https://www.acmicpc.net/problem/1707

import sys
from collections import deque

t = int(input())
for _ in range(t):
    v, e = map(int,input().split())
    l = {}
    for i in range(1,v+1):
        l[i] = set()
    for _ in range(e):
        a, b = map(int,sys.stdin.readline().split())
        l[a].add(b)
        l[b].add(a)
    
    graph = [-2]*(v+1)
    result = True
    for i in range(1,v+1):
        if graph[i] == -2:
            q = deque()
            q.append(i)
            graph[i] = 1

            while q:
                now = q.popleft()
                for c in l[now]:
                    if graph[c] == graph[now]:
                        result = False
                        break
                    elif graph[c] == -2:
                        graph[c] = -graph[now]
                        q.append(c)
        if result == False:
            break
    print('YES' if result else 'NO')
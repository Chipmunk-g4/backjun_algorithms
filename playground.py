"""
시간 초과
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
w = int(input())
p = [list(map(int,input().split())) for _ in range(w)]

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# dp[x][y] : 1번 경찰차가 x번째 사건을 완료했고, 2번 경찰차가 y번째 사건을 완료했을 때 최소 이동 거리
dp = [[[1e9, [-1,-1]] for _ in range(w+1)] for _ in range(w+1)]
dp[0][1] = [dist([n,n],p[0]), [0,0]]
dp[1][0] = [dist([1,1],p[0]), [0,0]]

for now in range(2, w + 1):
    # x == now-1인 경우 : y = 0 ~ x-1
    x = now-1
    for y in range(0, x):
        # 1번 차
        if dp[now][y][0] > dp[x][y][0] + dist(p[x-1],p[now-1]):
            dp[now][y] = [dp[x][y][0] + dist(p[x-1],p[now-1]), [x,y]]

        # 2번 차
        if dp[x][now][0] > dp[x][y][0] + dist([n,n] if y==0 else p[y-1],p[now-1]):
            dp[x][now] = [dp[x][y][0] + dist([n,n] if y==0 else p[y-1],p[now-1]), [x,y]]

    # y == now-1인 경우 : x = 0 ~ y-1
    y = now-1
    for x in range(0,y):
        # 1번 차
        if dp[now][y][0] > dp[x][y][0] + dist([1,1] if x==0 else p[x-1],p[now-1]):
            dp[now][y] = [dp[x][y][0] + dist([1,1] if x==0 else p[x-1],p[now-1]), [x,y]]

        # 2번 차
        if dp[x][now][0] > dp[x][y][0] + dist(p[y-1],p[now-1]):
            dp[x][now] = [dp[x][y][0] + dist(p[y-1],p[now-1]), [x,y]]

now = []
mv = 1e9
for i in range(w):
    if dp[i][w][0] < mv:
        mv = dp[i][w][0]
        now = [i,w]
    if dp[w][i][0] < mv:
        mv = dp[w][i][0]
        now = [w,i]

print(mv)

result = []
cnt = 0
bef = dp[now[0]][now[1]][1]
while cnt != w:
    if now[0] == bef[0]:
        result.append(2)
    else:
        result.append(1)
    now = bef
    bef = dp[now[0]][now[1]][1]
    cnt+=1

for v in reversed(result): print(v)
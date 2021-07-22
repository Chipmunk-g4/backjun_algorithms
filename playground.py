# https://www.acmicpc.net/problem/1520

import sys

m, n = map(int,input().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
dp = [[0 for _ in range(n)] for _ in range(m)]
dp[0][0] = 1

for i in range(m):
    for j in range(n):
        udlr = [[-1, [i-1, j]],[-1, [i+1, j]],[-1, [i, j-1]],[-1, [i, j+1]]] # up down left right
        udlr[0][0] = -1 if i-1 < 0 else board[i-1][j]
        udlr[1][0] = -1 if i >= m-1 else board[i+1][j]
        udlr[2][0] = -1 if j-1 < 0 else board[i][j-1]
        udlr[3][0] = -1 if j >= n-1 else board[i][j+1]

        for didx in [0, 2]: # up left
            if udlr[didx][0] != -1:
                if  udlr[didx][0] > board[i][j]:
                    dp[i][j] += dp[udlr[didx][1][0]][udlr[didx][1][1]]
        for didx in [0, 2]: # up left
            if udlr[didx][0] != -1:
                if  udlr[didx][0] < board[i][j]:
                    dp[udlr[didx][1][0]][udlr[didx][1][1]] += dp[i][j]

print(dp)
print(dp[m-1][n-1])
"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

4 5
50 45 37 32 30
35 50 27 20 25
30 30 25 17 28
27 24 22 15 10

7 5
30 99 99 99 99
29 28 27 26 25
99 99 99 99 24
17 18 19 99 23
16 99 20 21 22
15 99 99 99 99
14 13 12 11 10
"""
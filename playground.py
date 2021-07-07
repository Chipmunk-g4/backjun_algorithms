# https://www.acmicpc.net/problem/14889

import sys

t = int(input())
board = []
result = []

for _ in range(t):
    board.append(list(map(int,sys.stdin.readline().split())))

for x in range(t):
    for y in range(t):
        tmp = board[x][y] + board[y][x]
        board[x][y] = tmp
        board[y][x] = tmp

def calculator(team):
    team = list(team)
    result = 0
    for x in range(len(team)-1):
        for y in range(x+1,len(team)):
            result+=board[team[x]][team[y]]//2
    return result

def team_maker(remains, team):
    if len(remains) == len(team):
        result.append(abs(calculator(team)-calculator(remains)))
    else:
        for r in remains:
            remains.remove(r)
            team.add(r)
            team_maker(remains, team)
            remains.add(r)
            team.remove(r)

team_maker(set([i for i in range(t)]), set([]))
print(min(result))
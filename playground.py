# https://www.acmicpc.net/problem/1874

import sys

stack = []
inv = 0
result = []
success = True

t = int(input())
for _ in range(t):
    now = int(sys.stdin.readline())
    if now > inv:
        for i in range(inv, now):
            inv+=1
            stack.append(inv)
            result.append('+')
        stack.pop()
        result.append('-')
    else:
        if stack[-1] == now:
            stack.pop()
            result.append('-')
        else:
            success = False
            break

if success:
    for i in result:
        print(i)
else:
    print('NO')
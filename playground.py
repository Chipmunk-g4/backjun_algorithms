# https://www.acmicpc.net/problem/18258

import sys
from queue import Queue

q = Queue()
t = int(input())

for _ in range(t):
    c = list(sys.stdin.readline().split())

    if c[0] == 'push':
        q.put(int(c[1]))
    elif c[0] == 'pop':
        if q.empty():
            print(-1)
        else:
            print(q.get())
    elif c[0] == 'size':
        print(q.qsize())
    elif c[0] == 'empty':
        print(1 if q.empty() else 0)
    elif c[0] == 'front':
        if q.empty():
            print(-1)
        else:
            print(q.queue[0])
    elif c[0] == 'back':
        if q.empty():
            print(-1)
        else:
            print(q.queue[q.qsize()-1])
# https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int,input().split()))
l = [0]*n

for i in range(n):
    l[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            l[i] = max(l[i], l[j]+1)
print(max(l))
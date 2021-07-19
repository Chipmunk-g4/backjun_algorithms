# https://www.acmicpc.net/problem/2805

n, m = map(int,input().split())
logs = list(map(int,input().split()))

start = 0
end = max(logs)
while start <= end:
    mid = (end+start)//2
    result = sum([logs[i] - mid if logs[i] > mid else 0 for i in range(n)])
    if result >= m:
        start = mid+1
    else:
        end = mid-1
print(end)
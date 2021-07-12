# https://www.acmicpc.net/problem/13305

n = int(input())
road = list(map(int,input().split()))
cities = list(map(int,input().split()))

price = [0 for _ in range(len(road))]

now_price = 1000000001
for i in range(len(cities)-1):
    if cities[i] < now_price:
        now_price = cities[i]
    price[i] = now_price

print(sum([price[i]*road[i] for i in range(len(road))]))
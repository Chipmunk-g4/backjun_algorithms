# https://www.acmicpc.net/problem/3036

import math

n = int(input())
gears = list(map(int,input().split()))
ratio = [[0,0]]*(n-1)

gcd1 = math.gcd(gears[0], gears[1])
ratio[0] = [gears[0]//gcd1, gears[1]//gcd1]

for i in range(1, n-1):
    a = ratio[i-1][0]*gears[i]
    b = ratio[i-1][1]*gears[i+1]
    gcd = math.gcd(a,b)
    ratio[i] = [a//gcd,b//gcd]

for i in ratio:
    print(f"{i[0]}/{i[1]}")
# https://www.acmicpc.net/problem/10217
"""
1->v 의 M비용 이내의 최단거리
* 1->v 최단거리가 M비용 이하인 경우 정답
* 1->v 최단거리가 M비용 초과인 경우 1->a1->v, 1->a2->v, ... , 1->av-2->v 최단거리 중 M비용 이하 경로의 최솟값
  이때 1->ak->v 경로는 1->ak, ak->v의 문제로 생각 가능
"""

import sys
import heapq

t = int(input())
for _ in range(t):

    v, M, e = map(int,input().split())
    l = [[[1e9,1e9] for _ in range(v+1)] for _ in range(v+1)]
    for i in range(1,v+1): l[i][i] = [0,0]

    for _ in range(e):
        a,b,c,d = map(int,input().split())
        if l[a][b][0] > c:
            l[a][b] = [c,d]

    # 먼저 각 점들의 최단거리 및 그때의 비용 구하기
    for i in range(1,v+1):
        for a in range(1, v+1):
            for b in range(1, v+1):
                if l[a][i][0] + l[i][b][0] < l[a][b][0]:
                    l[a][b][0] = l[a][i][0] + l[i][b][0]
                    l[a][b][1] = l[a][i][1] + l[i][b][1]

    # 최단거리 중 M비용 이하인 최단거리 구하기
    def sp_underM(a,b,M,l): # a:기점 b:종점 M:한계비용
        if l[a][b][1] <= M:
            return l[a][b]

        result = [1e9,1e9]
        for k in range(a+1,b):
            p = l[a][k] if l[a][k][1] <= M else sp_underM(a,k,M,l)
            q = l[k][b] if l[k][b][1] <= M else sp_underM(k,b,M,l)
            nowc = p[0] + q[0]
            nowd = p[1] + q[1]
            if nowd <= M and nowc < result[0]:
                result = [nowc,nowd]

        l[a][b] = result
        return result

    r = sp_underM(1,v,M,l)[0]
    print('Poor KCM' if r == 1e9 else r)
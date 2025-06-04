# 저울

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if i == j:
            continue
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    print(cnt)
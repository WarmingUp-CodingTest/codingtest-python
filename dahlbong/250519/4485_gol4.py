# 녹색 옷 입은 애가 젤다지?

import sys, heapq
input = sys.stdin.readline

def get_min_cost(graph):
    n = len(graph)
    heap = [(graph[0][0], 0, 0)]
    costs = [[float('inf')] * n for _ in range(n)]
    costs[0][0] = graph[0][0]

    while heap:
        cost, x, y = heapq.heappop(heap)
        if cost > costs[x][y]:
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < len(graph[0]):
                new_cost = cost + graph[nx][ny]
                if new_cost < costs[nx][ny]:
                    costs[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))
    return costs[-1][-1]

cnt = 0
while True:
    cnt += 1
    N = int(input())
    if N == 0:
        break
    theives = [list(map(int, input().split())) for _ in range(N)]
    cost = get_min_cost(theives)

    print(f"Problem {cnt}: {cost}")

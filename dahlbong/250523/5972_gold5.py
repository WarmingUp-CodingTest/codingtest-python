# 택배배송 

import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cow = map(int, input().split())
    graph[start].append((cow, end))
    graph[end].append((cow, start))


def get_minimum_cow(start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    heap = [(0, 1)]

    while heap:
        cur_cows, cur = heapq.heappop(heap)
        if cur_cows > dist[cur]:
            continue
        
        for next_cows, next in graph[cur]:
            new_dist = cur_cows + next_cows

            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(heap, (new_dist, next))
    return dist[N]

print(get_minimum_cow(1))
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

dijkstra(1)

print(distance[N])

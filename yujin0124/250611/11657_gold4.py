import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
distance = [int(1e9)] * (N+1)

for _ in range(M):
  A, B, C = map(int, input().split())
  edges.append((A, B, C))

def bellmanFord(start):
  distance[start] = 0
  for i in range(N):
    for j in range(M):
      A, B, C = edges[j]
      if distance[A] != int(1e9) and distance[A] + C  < distance[B]:
        distance[B] = distance[A] + C
        if i == N-1:
          return False
  return True

if bellmanFord(1):
  for i in range(2, N+1):
    if distance[i] == int(1e9):
      print("-1")
    else:
      print(distance[i])
else:
  print("-1")
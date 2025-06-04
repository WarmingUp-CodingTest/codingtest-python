from collections import deque

def down(x):
  visited = [False] * (N+1)
  visited[x] = True
  q = deque([x])
  
  while q:
    cx = q.popleft()
    for i in range(1, N+1):
      if arr[cx][i] == 1 and not visited[i]:
        visited[i] = True
        q.append(i)
  
  result = set()
  for i in range(1, N+1):
    if not visited[i]:
      result.add(i)
  return result

def up(x):
  visited = [False] * (N+1)
  visited[x] = True
  q = deque([x])
  
  while q:
    cx = q.popleft()
    for i in range(1, N+1):
      if arr[cx][i] == 2 and not visited[i]:
        visited[i] = True
        q.append(i)
  
  result = set()
  for i in range(1, N+1):
    if not visited[i]:
      result.add(i)
  return result

N = int(input())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 2

for i in range(1, N+1):
  result = len(down(i) & up(i))
  print(result)
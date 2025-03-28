import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def make_union(x, y, unions):
  unions.append([x, y])
  visited[x][y] = True
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue
    if visited[nx][ny]:
      continue
    if l <= abs(populations[x][y] - populations[nx][ny]) <= r:
      make_union(nx, ny, unions)

n, l, r = map(int, input().split())

populations = []
for i in range(n):
  populations.append(list(map(int, input().split())))

day = 0
while True:
  visited = [[False] * n for _ in range(n)]
  check = False
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        unions = []
        make_union(i, j, unions)
      
      if len(unions) <= 1:
        continue
      check = True
      
      population_sum = 0
      for x, y in unions:
        population_sum += populations[x][y]
      new_population = population_sum // len(unions)
      for x, y in unions:
        populations[x][y] = new_population
  
  if not check:
    break
  day += 1
        
print(day)
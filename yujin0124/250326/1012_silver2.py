import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n, k = 0, 0, 0
field = [[0] * 55 for _ in range(55)]

def dfs(x, y):
  field[x][y] = 0
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= m or ny < 0 or ny >= n:
      continue
    if field[nx][ny] == 1:
      dfs(nx, ny)


t = int(input())
while t > 0:
  t -= 1
  
  m, n, k = map(int, input().split())
  for i in range(k):
    x, y = map(int, input().split())
    field[x][y] = 1
  
  earthworm = 0
  for i in range(m):
    for j in range(n):
      if field[i][j] == 1:
        earthworm += 1
        dfs(i, j)

  print(earthworm)

from collections import deque

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move(x, y, d, s):
  nx = (x - 1 + dx[d] * s) % n + 1
  ny = (y - 1 + dy[d] * s) % n + 1
  return nx, ny

def water_copy(x, y):
  count = 0
  
  for i in [2, 4, 6, 8]:
    nx, ny = x + dx[i], y + dy[i]
    if 1 <= nx <= n and 1 <= ny <= n and A[nx][ny] > 0:
      count += 1
  
  return count

n, m = map(int, input().split())
A = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
  row = list(map(int, input().split()))
  for j in range(1, n+1):
    A[i][j] = row[j-1]

clouds = deque([(n, 1), (n, 2), (n-1, 1), (n-1, 2)])

for i in range(m):
  d, s = map(int, input().split())
  
  move_clouds = []
  while clouds:
    x, y = clouds.popleft()
    nx, ny = move(x, y, d, s)
    A[nx][ny] += 1
    move_clouds.append((nx, ny))
  
  for x, y in move_clouds:
    A[x][y] += water_copy(x, y)
  
  prev_clouds = set(move_clouds)
  
  for i in range(1, n+1):
    for j in range(1, n+1):
      if A[i][j] >= 2 and (i, j) not in prev_clouds:
        A[i][j] -= 2
        clouds.append((i, j))

water = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    water += A[i][j]
print(water)
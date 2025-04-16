from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def find_fish(x, y, shark_size):
  visited = [[-1] * N for _ in range(N)]
  queue = deque([(x, y)])
  visited[x][y] = 0
  
  fish_list = []
  while queue:
    cx, cy = queue.popleft()
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
        if arr[nx][ny] <= shark_size:
          queue.append((nx, ny))
          visited[nx][ny] = visited[cx][cy] + 1
          if 0 < arr[nx][ny] < shark_size:
            fish_list.append((nx, ny, visited[nx][ny]))
  if fish_list:
    fish_list.sort(key=lambda x: (x[2], x[0], x[1]))
    return fish_list[0]
  else:
    return None

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

shark_x, shark_y = 0, 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 9:
      shark_x, shark_y = i, j
      arr[i][j] = 0

cx, cy = shark_x, shark_y
size = 2
count = 0
time = 0

while True:
  fish = find_fish(cx, cy, size)
  
  if fish is None:
    break
  
  nx, ny, distance = fish
  time += distance
  
  arr[nx][ny] = 0
  count += 1
  
  cx, cy = nx, ny
  
  if count == size:
    size += 1
    count = 0

print(time)
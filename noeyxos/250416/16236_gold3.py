from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n): 
    for j in range(n):
        if area[i][j] == 9: 
            x, y = i, j
            area[i][j] = 0


def bfs(x, y, size) : 
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    fish = []

    while q: 
        cx, cy = q.popleft()
        for i in range(4): 
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1: 
                if area[nx][ny] > size : 
                    continue
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
                if 0 < area[nx][ny] < size: 
                    fish.append((visited[nx][ny], nx, ny))
    return sorted(fish)

size = 2
eat = 0
time = 0

while True: 
    fish_list = bfs(x, y, size)
    if not fish_list: 
        break

    dist, nx, ny = fish_list[0]
    time += dist
    eat += 1
    area[nx][ny] = 0 
    x, y = nx, ny

    if eat == size: 
        size += 1 
        eat = 0 

print(time)
from collections import deque

r, c = map(int, input().split())

ground = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_sheep = 0
total_wolf = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    sheep = 0
    wolf = 0

    if ground[x][y] == 'o':
        sheep += 1
    elif ground[x][y] == 'v':
        wolf += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and ground[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    if ground[nx][ny] == 'o':
                        sheep += 1
                    elif ground[nx][ny] == 'v':
                        wolf += 1

    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf

for i in range(r):
    for j in range(c):
        if not visited[i][j] and ground[i][j] != '#':
            s, w = bfs(i, j)
            total_sheep += s
            total_wolf += w

print(total_sheep, total_wolf)
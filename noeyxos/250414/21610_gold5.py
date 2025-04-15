from collections import deque

n, m = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]


direction = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

clouds = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])

for d, s in moves:
    d -= 1
    next_clouds = deque()

    while clouds:
        x, y = clouds.popleft()
        nx = (x + direction[d][0] * s) % n
        ny = (y + direction[d][1] * s) % n
        A[nx][ny] += 1
        next_clouds.append((nx, ny))

    visited = [[False]*n for _ in range(n)]
    for x, y in next_clouds:
        visited[x][y] = True
        count = 0
        for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and A[nx][ny] > 0:
                count += 1
        A[x][y] += count


    clouds = deque()
    for i in range(n):
        for j in range(n):
            if A[i][j] >= 2 and not visited[i][j]:
                clouds.append((i,j))
                A[i][j] -= 2


print(sum(map(sum, A)))
    
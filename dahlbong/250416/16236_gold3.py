from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0 

shark_size = 2
eat_count = 0
timer = 0

def get_fish(x, y, shark_size):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    fishes = []
    min_dist = float('inf')

    while q:
        x, y, distance = q.popleft()
        if distance > min_dist:
            break

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    if 0 < graph[nx][ny] < shark_size:
                        fishes.append((distance+1, nx, ny))
                    q.append((nx, ny, distance+1))
    fishes.sort()
    return fishes
    
while True:
    eat_fish = get_fish(shark_x, shark_y, shark_size)
    if not eat_fish:
        break

    dist, fx, fy = eat_fish[0]
    timer += dist
    shark_x, shark_y = fx, fy
    graph[fx][fy] = 0
    eat_count += 1

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(timer)

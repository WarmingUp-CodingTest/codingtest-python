import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [list(map(int, input().split())) for _ in range(N)]
commands = deque([tuple(map(int, input().split())) for _ in range(M)])

dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

def move_clouds_and_rain(clouds):
    d, s = commands.popleft()
    dx, dy = dir[d-1]
    new_clouds = []

    for cx, cy in clouds:
        nx = (cx + dx * s) % N
        ny = (cy + dy * s) % N
        baskets[nx][ny] += 1
        new_clouds.append((nx, ny))
    return new_clouds

def copy_water(clouds):
    for x, y in clouds:
        cnt = 0
        for dx, dy in diag:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and baskets[nx][ny] > 0:
                cnt += 1
        baskets[x][y] += cnt

def make_cloud(clouds):
    clouds = set(clouds)
    new_clouds = []

    for i in range(N):
        for j in range(N):
            if (i, j) not in clouds and baskets[i][j] >= 2:
                new_clouds.append((i, j))
                baskets[i][j] -= 2
    return new_clouds


clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

while commands:
    clouds = move_clouds_and_rain(clouds)
    copy_water(clouds)
    clouds = make_cloud(clouds)

print(sum(map(sum, baskets)))

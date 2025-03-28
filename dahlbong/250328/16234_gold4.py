import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

def new_population(association, association_population):
    for x, y in association:
        population[x][y] = association_population // len(association)

def could_open_border(r, c, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque([(r, c)])
    visited[r][c] = True
    pop_sum = population[r][c]
    tmp = [(r, c)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if abs(population[x][y] - population[nx][ny]) >= L and abs(population[x][y] - population[nx][ny]) <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    tmp.append((nx, ny))
                    pop_sum += population[nx][ny]
    return(tmp, pop_sum)

def associate():
    global ans
    while True:
        visited = [[False] * N for _ in range(N)]
        moved = False

        for i in range(N):
            for j in range(N):
                if visited[i][j] == False:
                    group, total = could_open_border(i, j, visited)
                    if len(group) > 1:
                        new_population(group, total)
                        moved = True

        if not moved:
            return ans
        ans += 1

ans = 0
print(associate())
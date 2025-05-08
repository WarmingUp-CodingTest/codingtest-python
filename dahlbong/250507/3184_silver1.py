import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
land = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

def fight(x, y):
    global visited, land
    wolf, lamb = 0, 0

    if land[x][y] == 'v':
        wolf += 1
    elif land[x][y] == 'o':
        lamb += 1
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and land[nx][ny] != '#' and not visited[nx][ny]:
                if land[nx][ny] == 'v':
                    wolf += 1
                elif land[nx][ny] == 'o':
                    lamb += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    
    if lamb == 0 or wolf == 0:
        return lamb, wolf
        
    if lamb > wolf:
        wolf = 0
    else:
        lamb = 0
    return lamb, wolf

lamb, wolf = 0, 0
for i in range(R):
    for j in range(C):
        if land[i][j] != '#' and not visited[i][j]:
            visited[i][j] = True
            l, w = fight(i, j)
            lamb += l
            wolf += w

print(lamb, wolf)

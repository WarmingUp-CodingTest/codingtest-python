import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
yard = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_sheep = 0
total_wolves = 0

for i in range(r):
    for j in range(c):
        if visited[i][j] or yard[i][j] == '#':
            continue
        
        sheep = 0
        wolves = 0
        
        queue = deque([(i, j)])
        visited[i][j] = True
        
        while queue:
            x, y = queue.popleft()
            
            if yard[x][y] == 'o':
                sheep += 1
            elif yard[x][y] == 'v':
                wolves += 1
            
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and yard[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        if sheep > wolves:
            total_sheep += sheep
        else:
            total_wolves += wolves

print(total_sheep, total_wolves)
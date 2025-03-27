import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def how_many_worms(r, c):
    if visited[r][c] == True:
        return
    
    global worms
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque([(r, c)])

    while q:
        xy = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + xy[0], dy[i] + xy[1]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                visited[nx][ny] = True   
    worms += 1

while T:
    T -= 1

    M, N, K = map(int, input().split())
    lettuce = []
    for _ in range(K):
        lettuce.append(tuple(map(int, input().split())))
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    worms = 0

    for i in range(M):
        for j in range(N):
            if (i, j) in lettuce:
                graph[j][i] = 1
    
    while lettuce:
        i, j = lettuce.pop()
        how_many_worms(j, i)

    print(worms)


    
    
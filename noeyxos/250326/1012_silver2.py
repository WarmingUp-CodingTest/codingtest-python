import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]


def dfs(row, col):
    if row < 0 or row >= n or col < 0 or col >= m or land[row][col] == 0  or visited[row][col]: 
        return 
    
    visited[row][col] = True
    for i in range(4): 
        nr, nc = row + dr[i] , col + dc[i]
        dfs(nr, nc)


t = int(input())

for _ in range(t): 
    m, n, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int,input().split())
        land[y][x] = 1

    count = 0 
    for row in range(n): 
        for col in range(m): 
            if land[row][col] == 1 and visited[row][col] == False:
                dfs(row, col) 
                count += 1

    print(count)
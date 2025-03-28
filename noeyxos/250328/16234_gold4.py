from collections import deque


n, l, r = map(int,input().split())
world = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n  for _ in range(n)]

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]


def bfs(start_r, start_c): 
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    union = [(start_r, start_c)]

    while queue: 
        r, c = queue.popleft()

        for i in range(4): 
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False:
                if l <= abs(world[r][c] - world[nr][nc]) <= r: 
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    union.append((nr, nc))

    if len(union) > 1 :
        return True
    return False

        
def open_border(): 
    days = 0
    while True:
        moved = False

        for i in range(n): 
            for j in range(n): 
                if visited[i][j] == False:
                    if bfs(i, j): 
                        moved = True

        if not moved: 
            break
        days += 1

    return days


print(open_border())
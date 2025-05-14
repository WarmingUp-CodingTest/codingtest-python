import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
max_sum = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, depth, total):
    global max_sum
    if depth == 4:
        max_sum = max(max_sum, total)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, total + board[nx][ny])
            visited[nx][ny] = False

# ㅗ, ㅜ, ㅓ, ㅏ 모양 체크 (DFS로 커버 못하는 경우)
def check_shape(x, y):
    global max_sum
    for shape in  [
        [(0,0), (0,1), (0,2), (1,1)],  # ㅜ
        [(0,0), (1,0), (2,0), (1,1)],  # ㅏ
        [(0,0), (0,1), (0,2), (-1,1)], # ㅗ
        [(0,0), (1,0), (2,0), (1,-1)]  # ㅓ
    ]:
        try:
            total = 0
            for dx, dy in shape:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0:
                    raise IndexError
                total += board[nx][ny]
            max_sum = max(max_sum, total)
        except IndexError:
            continue

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])   # DFS로 ㅗ 제외한 4가지 모양 체크
        visited[i][j] = False
        check_shape(i, j)           # ㅗ 모양 체크

print(max_sum)
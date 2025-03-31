import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, -1), (1, 0), (1, 1)]

def boost(x, y, cur_dir):
    if x == N - 1:
        return graph[x][y]

    min_cost = float('inf')
    for i in range(3):
        if cur_dir != i and 0 <= y + dxy[i][1] < M:
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            cost = boost(nx, ny, i) + graph[x][y]
            min_cost = min(min_cost, cost)
    return min_cost

ans = float('inf')

for i in range(M):
    ans = min(ans, boost(0, i, -1))

print(ans)
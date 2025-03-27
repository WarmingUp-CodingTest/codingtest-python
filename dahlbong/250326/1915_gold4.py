n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
   
dp = [[0] * m for _ in range(n)]
max_size = 0

for i in range(n):
    if graph[i][0] == '1':
        dp[i][0] = 1
        max_size = 1

for j in range(m):
    if graph[0][j] == '1':
        dp[0][j] = 1
        max_size = 1

for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == '1':
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            max_size = max(max_size, dp[i][j])

print(max_size ** 2)
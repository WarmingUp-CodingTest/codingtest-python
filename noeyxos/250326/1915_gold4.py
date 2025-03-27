n , m = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

max_square = 0

for i in range(n):
    for j in range(m): 
        if graph[i][j] == 1  : 
            if i == 0 or j == 0 : 
                dp[i][j] = 1
            else: 
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            max_square = max(max_square, dp[i][j])

print(max_square ** 2)
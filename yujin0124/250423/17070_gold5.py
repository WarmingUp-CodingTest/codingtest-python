n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        if (i==0 and j==1) or house[i][j] == 1: continue
        if j > 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
        if i > 0:
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
        if i > 0 and j > 0 and house[i-1][j] == 0 and house[i][j-1] == 0:
            dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))
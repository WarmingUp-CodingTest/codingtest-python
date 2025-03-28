import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if i == 0 or j == 0:
      dp[i][j] = array[i][j]
      continue
    
    if array[i][j] == 0:
      dp[i][j] = 0
    else:
      dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

max = 0
for i in range(n):
  for j in range(m):
      if dp[i][j] > max:
        max = dp[i][j]

print(max * max)
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
blocks = []
for i in range(N):
  blocks.append(list(map(int, input().split())))
dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
  for j in range(H+1):
    dp[i][j] = dp[i-1][j] % 10007
    for k in range(len(blocks[i-1])):
      block_length = blocks[i-1][k]
      if block_length <= j:
        dp[i][j] = (dp[i][j] + dp[i-1][j - block_length]) % 10007

print(dp[N][H] % 10007)
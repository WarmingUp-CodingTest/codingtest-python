n = int(input())
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
if n > 1:
  dp[2] = 2
if n > 2:
  for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

m = int(input())
prev = 0
result = 1
for i in range(m):
  vip = int(input())
  result *= dp[vip - prev - 1]
  prev = vip
result *= dp[n - prev]

print(result)
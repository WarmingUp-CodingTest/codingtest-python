n = int(input())
arr = [0] * n

dp = [0] * n
for i in range(n):
  arr[i] = int(input())
  dp[i] = 1
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
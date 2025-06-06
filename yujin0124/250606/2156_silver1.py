import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for i in range(n):
  arr.append(int(input()))
dp = [0] * 10010

dp[1] = arr[1]
if n >= 2:
  dp[2] = arr[1] + arr[2]

for i in range(3, n+1):
  dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

print(max(dp))
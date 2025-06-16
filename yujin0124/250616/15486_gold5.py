import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(1, N+1):
  T, P = map(int, input().split())
  
  if i > 1:
    dp[i] = max(dp[i], dp[i-1])
    
  if i-1+T <= N:
    dp[i-1+T] = max(dp[i-1+T], dp[i-1] + P)

print(dp[-1])
import sys
input = sys.stdin.readline

n, d = map(int, input().split())
dp = [i for i in range(d+1)]
  
jirumgils = []
for i in range(n):
  start, end, distance = map(int, input().split())
  if end - start > distance:
    jirumgils.append([start, end, distance])

jirumgils.sort(key = lambda x:x[0])

for start, end, distance in jirumgils:
  if start <= d and end <=d:
    dp[end] = min(dp[end], dp[start]+distance)
    for i in range(1, d+1):
      dp[i] = min(dp[i], dp[i-1]+1)

print(dp[d])
import sys
input = sys.stdin.readline
N = int(input())

scores = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    minimum = scores[i]
    maximum = scores[i]
    for j in range(i+1, N):
        minimum = min(minimum, scores[j])
        maximum = max(maximum, scores[j])
        dp[j] = max(dp[j], maximum - minimum + dp[i-1])

print(dp[-1])
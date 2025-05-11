import sys
input = sys.stdin.readline

MAX = 10001
dp = [0] * MAX
dp[0] = 1

for i in [1, 2, 3]:
    for j in range(i, MAX):
        dp[j] += dp[j - i]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
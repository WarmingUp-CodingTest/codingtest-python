N, D = map(int, input().split())
shortcuts = []
for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:
        shortcuts.append([s, e, d])

dp = [i for i in range(D+1)]

for d in range(D+1):
    dp[d] = min(dp[d], dp[d-1] + 1)
    for start, end, distance in shortcuts:
        if d == start:
            dp[end] = min(dp[end], dp[start] + distance)

print(dp[-1])

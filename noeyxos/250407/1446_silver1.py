n, d = map(int, input().split())

route = []
for _ in range(n):
    start, end, length = map(int, input().split())
    if end <= d and end - start > length:
        route.append((start, end, length))

dp = [i for i in range(d+1)]

for i in range(d+1):
    if i != 0: 
        dp[i] = min(dp[i], dp[i-1]+1)

    for start, end, length in route:
        if start == i and end <= d: 
            dp[end] = min(dp[end], dp[start] + length)


print(dp[d])
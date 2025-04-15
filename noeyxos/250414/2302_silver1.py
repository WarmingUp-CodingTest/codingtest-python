n = int(input())
m = int(input())

vip_seats = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1): 
    dp[i] = dp[i-1] + dp[i-2]

result = 1 
last_vip = 0

for vip in vip_seats: 
    gap = vip - last_vip - 1
    result *= dp[gap]
    last_vip = vip

gap = n - last_vip
result *= dp[gap]

print(result)


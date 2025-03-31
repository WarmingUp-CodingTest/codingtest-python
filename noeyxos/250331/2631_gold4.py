n = int(input())
students = [int(input()) for _ in range(n)]

dp = [1] * n

for i in range(1, n): 
    for j in range(i): 
        if students[i] > students[j]:
            dp[i] = max(dp[i], dp[j] + 1)

moves = max(dp)

print(n - moves)
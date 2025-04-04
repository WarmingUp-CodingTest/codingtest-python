n = int(input())
students =list(map(int, input().split()))
dp = [0] * n


for i in range(n): 
    max_score = students[i]
    min_score = students[i]

    for j in range(i, -1, -1):
        max_score = max(max_score, students[j])
        min_score = min(min_score, students[j])
        score = max_score - min_score

        if j > 0:
            dp[i] = max(dp[i], dp[j-1] + score)
        else:
            dp[i] = max(dp[i], score)

print(dp[n-1])
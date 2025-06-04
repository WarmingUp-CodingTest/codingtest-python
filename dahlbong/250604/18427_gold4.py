N, M, H = map(int, input().split())

# 학생별 블록 목록 (1-based index)
blocks = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    blocks[i] = list(map(int, input().split()))

MOD = 10007

# dp[i][j] = i명의 학생을 사용해 높이 j를 만드는 경우의 수
dp = [[0] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 1  # 아무 학생도 사용하지 않고 높이 0 만드는 경우 1가지

# DP 테이블 채우기
for i in range(1, N + 1):  # i명까지 사용
    for j in range(H + 1):  # 현재 높이 j
        # i번째 학생이 블록을 사용하지 않는 경우
        dp[i][j] = dp[i - 1][j] % MOD

        # i번째 학생이 자기 블록 중 하나를 사용하는 경우
        for h in blocks[i]:
            if j - h >= 0:
                dp[i][j] += dp[i - 1][j - h]
                dp[i][j] %= MOD

print(dp[-1][-1])
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jumps = {int(x): int(y) for _ in range(N + M) for x, y in [input().split()]}

dp = [float('inf')] * 101
dp[1] = 0

for cur in range(1, 100):
    for dice in range(1, 7):
        if cur + dice <= 100:
            next = cur + dice

            if next in jumps:
                next = jumps[next]
            dp[next] = min(dp[next], dp[cur] + 1)

    for re in range(1, cur + 1):
        for dice in range(1, 7):
            if re + dice <= 100:
                next = re + dice
                
                if next in jumps:
                    next = jumps[next]
                dp[next] = min(dp[next], dp[re] + 1)

print(dp[100])
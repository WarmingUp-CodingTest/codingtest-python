import sys

input = sys.stdin.readline
N = int(input())
expected_rank = [int(input()) for _ in range(N)]
ans = 0

expected_rank.sort()

for i in range(N):
    ans += abs(expected_rank[i] - (i + 1))

print(ans)
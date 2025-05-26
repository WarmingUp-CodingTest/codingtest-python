# 랜선 자르기

import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
start, end = 1, sum(lans) // N

while start <= end:
    total_lines = 0
    mid = (start + end) // 2
    for lan in lans:
        total_lines += lan // mid
    if total_lines >= N:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
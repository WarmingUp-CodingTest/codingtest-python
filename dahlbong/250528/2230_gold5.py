#2230 수고르기

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted([int(input()) for _ in range(N)])

left, right = 0, 0
ans = float('inf')
while left <= right:
    if nums[right] - nums[left] < M:
        if right == N-1:
            break
        right += 1
    else:
        ans = min(ans, nums[right] - nums[left])
        left += 1

print(ans)
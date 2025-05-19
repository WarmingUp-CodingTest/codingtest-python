# 숫자고르기

import sys
input = sys.stdin.readline
N = int(input())
nums = [0] + [int(input()) for _ in range(N)]
ans = []

cnt = N

while True:
    is_ans = True
    for i in range(1, N + 1):
        if nums[i] == 0:
            continue
        if i not in nums:
            nums[i] = 0
            cnt -= 1
            is_ans = False
    if is_ans:
        break

print(cnt)
ans = sorted(num for num in nums if num != 0)
print(*ans, sep='\n')

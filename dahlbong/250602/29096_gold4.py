# 내려가기
import sys
input = sys.stdin.readline
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

max_dp_prev = nums[0][:]
min_dp_prev = nums[0][:]

for i in range(1, N):
    a, b, c = nums[i]
    
    max_dp_cur = [
        max(max_dp_prev[0], max_dp_prev[1]) + a,
        max(max_dp_prev[0], max_dp_prev[1], max_dp_prev[2]) + b,
        max(max_dp_prev[1], max_dp_prev[2]) + c
    ]
    
    min_dp_cur = [
        min(min_dp_prev[0], min_dp_prev[1]) + a,
        min(min_dp_prev[0], min_dp_prev[1], min_dp_prev[2]) + b,
        min(min_dp_prev[1], min_dp_prev[2]) + c
    ]
    
    max_dp_prev = max_dp_cur
    min_dp_prev = min_dp_cur

print(max(max_dp_prev), min(min_dp_prev))
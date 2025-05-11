import sys
from collections import defaultdict
input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().split()))
max_length = 0

counts = defaultdict(int)
left = 0
max_length = 0

for right in range(N):
    counts[nums[right]] += 1

    while counts[nums[right]] > K:
        counts[nums[left]] -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
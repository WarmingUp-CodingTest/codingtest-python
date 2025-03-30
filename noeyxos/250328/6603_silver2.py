from itertools import combinations
import sys

cases = []

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums == [0]:
        break
    cases.append(nums[1: ])

for case in cases:
    for combi in combinations(case, 6):
        print(*combi)
    print()
#다이어트

import heapq
G = int(input())

sums_subtracts = []
nums = [i for i in range(1, G+1)]
ans = []

for i in range(1, int(G**0.5)+1):
    if G % i != 0:
        continue
    sum_ = G // i
    subtract = i

    if (sum_ + subtract) % 2 != 0:
        continue

    y = (sum_ + subtract) // 2
    x = (sum_ - subtract) // 2

    if x > 0:
        ans.append(y)

if ans:
    ans.sort()
    for y in ans:
        print(y)
else:
    print(-1)
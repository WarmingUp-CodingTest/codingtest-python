import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
chicken_distance = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

for c in chicken:
    tmp_distance = []
    for h in house:
        tmp_distance.append(abs(c[0] - h[0]) + abs(c[1] - h[1]))
    chicken_distance.append(tmp_distance)
chicken_candidates = list(combinations(chicken_distance, M))

ans = float('inf')
for c in chicken_candidates:
    cur_disance = 0
    for z in zip(*c):
        cur_disance += min(z)
    ans = min(cur_disance, ans)

print(ans)
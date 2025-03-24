import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int,input().split())
chicken_shops, houses = [], []

for i in range(n):
  maps = list(map(int, input().split()))
  for j in range(n):
    if maps[j] == 1:
        houses.append([i, j])
    elif maps[j] == 2:
        chicken_shops.append([i, j])

chicken_distance_min = 99999999
for shop in combinations(chicken_shops, m):
  sum = 0
  for house in houses:
    chicken_distance = 999999
    for i in range(m):
      chicken_distance = min(chicken_distance, abs(house[0] - chicken_shops[j][0]) + abs(house[1] - chicken_shops[j][1]))
    sum += chicken_distance
  chicken_distance_min = min(chicken_distance_min, sum)

print(chicken_distance_min)
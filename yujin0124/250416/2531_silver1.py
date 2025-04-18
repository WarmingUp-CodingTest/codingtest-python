import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushis = []
for i in range(N):
  sushi = int(input())
  sushis.append(sushi)


check = [0] * (d+1)
count = 0

for i in range(k):
  if check[sushis[i]] == 0:
    count += 1
  check[sushis[i]] += 1
max_count = count + (1 if check[c] == 0 else 0)

for i in range(N):
  check[sushis[i]] -= 1
  if check[sushis[i]] == 0:
    count -= 1
  
  new_idx = (i + k) % N
  if check[sushis[new_idx]] == 0:
    count += 1
  check[sushis[new_idx]] += 1
  
  current_count = count + (1 if check[c] == 0 else 0)
  max_count = max(max_count, current_count)

print(max_count)
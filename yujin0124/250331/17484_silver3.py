import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1, 1]
dy = [-1, 0, 1]

min_price = n * 110

def back(prev, sum, x, y):
  global min_price
  
  sum += prices[x][y]
  if min_price < sum:
    return
  
  if x >= n-1:
    min_price = min(min_price, sum)
    return
  
  for i in range(3):
    if prev == i:
      continue
    nx, ny = x + dx[i], y + dy[i]
    if not(0 <= nx < n and 0 <= ny < m):
      continue
    back(i, sum, nx, ny)


for i in range(m):
  back(-1, 0, 0, i)

print(min_price)
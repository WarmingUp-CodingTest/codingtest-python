import sys, heapq
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
  heapq.heappush(hq, int(input()))

result = 0
while len(hq) > 1:
  x = heapq.heappop(hq)
  y = heapq.heappop(hq)
  
  heapq.heappush(hq, x+y)
  result += (x+y)

print(result)
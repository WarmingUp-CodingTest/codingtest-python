import sys
input = sys.stdin.readline

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
result = sys.maxsize

def back(index, count):
  global result
  
  if count == n//2:
    start = 0
    link = 0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]:
          start += stats[i][j]
          continue
        
        if not visited[i] and not visited[j]:
          link += stats[i][j]
      
    result = min(abs(start - link), result)
    return
  
  if index == n:
    return
  
  visited[index] = True
  back(index + 1, count + 1)
  visited[index] = False
  back(index + 1, count)

back(0, 0)
print(result)
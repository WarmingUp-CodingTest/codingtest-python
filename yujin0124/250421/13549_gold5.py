from collections import deque

n, k = map(int, input().split())

visited = [float('inf')] * 100100
que = deque()
que.append(n)
visited[n] = 0

while que:
    x = que.popleft()
    
    if x*2 <= 100_000 and visited[x*2] > visited[x]:
        visited[x*2] = visited[x] 
        que.appendleft(x*2)
        
    if x-1 >= 0 and visited[x-1] > visited[x] + 1:
        visited[x-1] = visited[x] + 1
        que.append(x-1)
        
    if x+1 <= 100_000 and visited[x+1] > visited[x] + 1:
        visited[x+1] = visited[x] + 1
        que.append(x+1)

print(visited[k])
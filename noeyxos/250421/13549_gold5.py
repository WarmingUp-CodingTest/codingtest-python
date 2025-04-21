from collections import deque


n, k = map(int, input().split())

def hide_and_seek(n, k):
    visited = {}
    q = deque()
    q.append(n)
    visited[n] = 0


    while q: 
        current = q.popleft()

        if current == k : 
            return visited[current]
        
        if 0 <= 2 * current < 100000 and 2 * current not in visited:
            visited[2*current] = visited[current]
            q.appendleft(2*current)

        for next in [current - 1, current + 1]:
            if 0 <= next < 100000 and next not in visited:
                visited[next] = visited[current] + 1
                q.append(next)

print(hide_and_seek(n, k))
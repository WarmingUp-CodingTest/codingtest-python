from collections import deque

def bfs(a, b, c):
    sum = a + b + c
    if sum % 3 != 0:
        return 0
    
    visited = [[False] * 1501 for _ in range(1501)]
    q = deque([(a, b)])
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        z = sum - x - y
        if x == y == z:
            return 1
        
        for i, j in ((x, y), (y, z), (x, z)):
            if i == j:
                continue
            big, small = max(i, j), min(i, j)
            ns, nb = 2 * small, big - small
            new = [ns, nb, sum-ns-nb]
            new.sort()

            if not visited[new[0]][new[1]]:
                visited[new[0]][new[1]] = True
                q.append((new[0], new[1]))
    return 0

A, B, C = map(int, input().split())
init = sorted([A, B, C])
print(bfs(init[0], init[1], init[2]))

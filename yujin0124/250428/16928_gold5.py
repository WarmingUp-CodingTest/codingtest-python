from collections import deque

def sol():
    N, M = map(int, input().split())
    
    board = {}
    
    for _ in range(N):
        x, y = map(int, input().split())
        board[x] = y
    
    for _ in range(M):
        u, v = map(int, input().split())
        board[u] = v
    
    visited = [False] * 101
    queue = deque([(1, 0)])
    visited[1] = True
    
    while queue:
        pos, throws = queue.popleft()
        
        if pos == 100:
            return throws
        
        for dice in range(1, 7):
            next_pos = pos + dice
            
            if next_pos > 100:
                continue
            
            if next_pos in board:
                next_pos = board[next_pos]
            
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, throws + 1))
    
    return -1

print(sol())
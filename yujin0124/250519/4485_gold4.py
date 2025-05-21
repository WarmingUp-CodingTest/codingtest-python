import sys
import heapq

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def sol():
    p = 0
    
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break  
        p += 1
        
        cave = []
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().strip().split()))
            cave.append(row)
            
        pq = [(cave[0][0], 0, 0)]
        distance = [[float('inf')] * n for _ in range(n)]
        distance[0][0] = cave[0][0]
        
        while pq:
            loss, x, y = heapq.heappop(pq)
            
            if loss > distance[x][y]:
                continue

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < n:
                    new_loss = loss + cave[nx][ny]
                    
                    if new_loss < distance[nx][ny]:
                        distance[nx][ny] = new_loss
                        heapq.heappush(pq, (new_loss, nx, ny))
        
        print(f"Problem {p}: {distance[n-1][n-1]}")

sol()
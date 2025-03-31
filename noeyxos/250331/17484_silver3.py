import sys
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
route =[list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1]
dc = [1, 1, 1]

min_fuel = float('inf')

def is_valid_direction(row, col): 
    return 0 <= row < n and 0 <= col < m

def dfs(row, col, fuel, prev_direction):
    global min_fuel

    if row == n - 1: 
        min_fuel = min(min_fuel, fuel)
        print("min_fuel" + min_fuel)
        return

    for i in range(3): 
        if i != prev_direction: 
            nr, nc = row + dr[i], col + dc[i]
            if is_valid_direction(nr, nc):
                dfs(nr, nc, fuel + route[nr][nc], i)

for col in range(m): 
    dfs(0, col, route[0][col], -1)
        
print(min_fuel)
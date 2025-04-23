import sys
sys.setrecursionlimit(10**6)

n = int(input())
floor = [list(map(int, input().split())) for _ in range(n)]

count = 0

direction =  [(0,1), (1,0), (1,1)]

def move_pipes(x, y, direction): 
    global count

    if x == n - 1 and y == n - 1 : 
        count += 1
        return 
    
    if direction == 0 or direction == 2 :
        nx, ny = x , y + 1
        if ny < n and floor[nx][ny] == 0 :
            move_pipes(nx, ny, 0)

    if direction == 1 or direction == 2 :
        nx, ny = x + 1 , y
        if nx < n and floor[nx][ny] == 0 :
            move_pipes(nx, ny, 1)

    nx, ny = x + 1, y + 1
    if nx < n and ny < n : 
        if floor[nx][ny] == 0 and floor[x][ny] == 0 and floor[nx][y] == 0 :
            move_pipes(nx, ny, 2)

move_pipes(0, 1, 0)
print(count)
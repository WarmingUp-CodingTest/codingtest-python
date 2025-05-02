import sys
input = sys.stdin.readline

dice = [0, 0, 0, 0, 0, 0, 0]
next_top = [0, 4, 3, 5, 2]
next_bottom = [0, 3, 4, 2, 5]

def roll_dice(direction):
  nt = next_top[direction]
  nb = next_bottom[direction]
  
  temp = dice[nb]
  dice[nb] = dice[1]
  dice[1] = dice[nt]
  dice[nt] = dice[6]
  dice[6] = temp

def can_move(nx, ny, n, m):
    return 0 <= nx < n and 0 <= ny < m

def move(direction, x, y):
    if direction == 1:
        return x, y+1
    if direction == 2:
        return x, y-1
    if direction == 3:
        return x-1, y
    if direction == 4:
        return x+1, y

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

for command in commands:
    nx, ny = move(command, x, y)
    
    if can_move(nx, ny, n, m):
        x, y = nx, ny
        
        roll_dice(command)
        
        if maps[x][y] == 0:
            maps[x][y] = dice[6]
        else:
            dice[6] = maps[x][y]
            maps[x][y] = 0
            
        print(dice[1])
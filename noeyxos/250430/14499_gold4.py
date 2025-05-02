import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0] * 6

def rotate(dir):
    top, north, east, west, south, bottom = dice
    if dir == 1:
        dice[0], dice[2], dice[5], dice[3] = west, top, east, bottom
    elif dir == 2:
        dice[0], dice[2], dice[5], dice[3] = east, bottom, west, top
    elif dir == 3:
        dice[0], dice[1], dice[5], dice[4] = south, top, north, bottom
    elif dir == 4:
        dice[0], dice[1], dice[5], dice[4] = north, bottom, south, top

for d in orders:
    nx, ny = x + dx[d], y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    x, y = nx, ny
    rotate(d)
    
    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0

    print(dice[0])
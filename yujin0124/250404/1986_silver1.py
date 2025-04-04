import sys
input = sys.stdin.readline

qx = [-1, -1, -1, 0, 0, 1, 1, 1]
qy = [-1, 0, 1, -1, 1, -1, 0, 1]

def move_queen(x, y):
  can_move = [True] * 8
  step = 1
  while 1:
    check = False
    for i in range(8):
      if can_move[i]:
        nx, ny = x + qx[i] * step, y + qy[i] * step
        if not(0 < nx <= m and 0 < ny <= n):
          can_move[i] = False
          continue
        if chess[nx][ny] > 0:
          can_move[i] = False
          continue
        chess[nx][ny] = -1
        check = True
    if not check:
      break
    step += 1

kx = [-2, -1, 1, 2, 2, 1, -1, -2]
ky = [-1, -2, -2, -1, 1, 2, 2, 1]
def move_knight(x, y):
  for i in range(8):
    nx, ny = x + kx[i], y + ky[i]
    if not(0 < nx <= m and 0 < ny <= n):
      continue
    if chess[nx][ny] > 0:
      continue
    chess[nx][ny] = -1

n, m = map(int, input().split())
chess = [[0] * (n+1) for _ in range(m+1)]
queens = list(map(int, input().split()))
knights = list(map(int, input().split()))
pawns = list(map(int, input().split()))

for i in range(queens[0]):
  chess[queens[i*2+2]][queens[i*2+1]] = 1
for i in range(knights[0]):
  chess[knights[i*2+2]][knights[i*2+1]] = 1
for i in range(pawns[0]):
  chess[pawns[i*2+2]][pawns[i*2+1]] = 1

for i in range(queens[0]):
  move_queen(queens[i*2+2], queens[i*2+1])
for i in range(knights[0]):
  move_knight(knights[i*2+2], knights[i*2+1])

safe = 0
for i in range(1, m+1):
  for j in range(1, n+1):
    if chess[i][j] == 0:
      safe += 1
print(safe)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

def parse_pieces():
    data = list(map(int, input().split()))
    count = data[0]
    pieces = [[r-1, c-1] for r, c in zip(data[1::2], data[2::2])]
    return count, pieces

def set_safe(lists):
    for x, y in lists:
        is_dangerous[x][y] = -1

def move_knight(r, c):
    for dx, dy in dk:
        x, y = r + dx, c + dy
        if 0 <= x < n and 0 <= y < m and is_dangerous[x][y] == False:
            is_dangerous[x][y] = True

def move_queen(r, c):
    for dx, dy in dq:
        x, y = r, c

        while True:
            x += dx
            y += dy
            if not (0 <= x < n and 0 <= y < m):
                break
            if is_dangerous[x][y] == -1:
                break
            is_dangerous[x][y] = True

q, queens = parse_pieces()
k, knights = parse_pieces()
p, pawns = parse_pieces()

is_dangerous = [[False] * m for _ in range(n)]
set_safe(queens)
set_safe(knights)
set_safe(pawns)

dk = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
dq = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]

for x, y in queens:
    move_queen(x, y)
for x, y in knights:
    move_knight(x, y)

safe = sum(1 for i in range(n) for j in range(m) if is_dangerous[i][j] == False)
print(safe)
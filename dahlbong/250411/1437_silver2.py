n = int(input())
commands = input()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]  # 남 - 서 - 북 - 동

x, y = 0, 0
dir = 0 
path = [(x, y)]

for cmd in commands:
    if cmd == 'F':
        x += dx[dir]
        y += dy[dir]
        path.append((x, y))
    elif cmd == 'L':
        dir = (dir + 3) % 4
    elif cmd == 'R':
        dir = (dir + 1) % 4

min_x = min(pos[0] for pos in path)
max_x = max(pos[0] for pos in path)
min_y = min(pos[1] for pos in path)
max_y = max(pos[1] for pos in path)

rows = max_x - min_x + 1
cols = max_y - min_y + 1
maze = [['#'] * cols for _ in range(rows)]

for px, py in path:
    maze[px - min_x][py - min_y] = '.'

for row in maze:
    print(*row, sep='')

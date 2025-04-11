n = int(input())
actions = list(input().strip())

x, y = 0, 0
visited = [(x, y)]

direction = [(1, 0) , (0, -1), (-1, 0), (0, 1)]
dir_idx = 0
for action in actions: 
    if action == 'R' : 
        dir_idx = (dir_idx + 1) % 4
    elif action == 'L' : 
        dir_idx = (dir_idx - 1) % 4
    elif action == 'F' :
        dx, dy = direction[dir_idx]
        x += dx
        y += dy
        visited.append((x, y))

min_x = min(x for x, y in visited)
max_x = max(x for x, y in visited)
min_y = min(y for x, y in visited)
max_y = max(y for x, y in visited)

rows = max_x - min_x + 1
cols = max_y - min_y + 1
maze = [['#'] * cols for _ in range(rows)]

for x, y in visited:
    maze[x - min_x][y - min_y] = '.'

for row in maze:
    print(''.join(row)) 
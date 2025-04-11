n = int(input())
moves = input()
cells = [[0, 0]]
hongjun_x, hongjun_y = 0, 0

directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
face = 0

def rotate(rotate_direction, face) -> int:
  if rotate_direction == 'R':
    face += 1
  else:
    face -= 1
  return face % 4
 
for move in moves:
  if move == 'F':
    hongjun_x += directions[face][0]
    hongjun_y += directions[face][1]
    
    cells.append([hongjun_x, hongjun_y])
  else:
    face = rotate(move, face)

max_x, max_y = -100, -100
min_x, min_y = 100, 100

for cell in cells:
  max_x = max(max_x, cell[0])
  min_x = min(min_x, cell[0])
  max_y = max(max_y, cell[1])
  min_y = min(min_y, cell[1])

height = max_x - min_x + 1
width = max_y - min_y + 1

for cell in cells:
    cell[0] -= min_x
    cell[1] -= min_y

result = [['#'] * width for _ in range(height)]
for cell in cells:
  result[cell[0]][cell[1]] = "."

for i in range(height):
    for j in range(width):
        print(result[i][j], end="")
    print()
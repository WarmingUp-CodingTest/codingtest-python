R, C, N = map(int, input().split())

arr = [list(input().strip()) for _ in range(R)]

if N == 1:
  for row in arr:
    print(''.join(row))
elif N % 2 == 0:
  for i in range(R):
    print('O' * C)
else:
  bombs = []
  for i in range(R):
    for j in range(C):
      if arr[i][j] == 'O':
        bombs.append((i, j))
      arr[i][j] = 'O'
  
  for x, y in bombs:
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < R and 0 <= ny < C:
        arr[nx][ny] = '.'
  
  if N % 4 == 1:
      bombs = []
      for i in range(R):
        for j in range(C):
          if arr[i][j] == 'O':
            bombs.append((i, j))
          arr[i][j] = 'O'
      
      for x, y in bombs:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
          nx, ny = x + dx, y + dy
          if 0 <= nx < R and 0 <= ny < C:
            arr[nx][ny] = '.'
  
  for row in arr:
    print(''.join(row))
  
R, C, N = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(input().strip()))

def explode(board):
        explode_pos = []
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    explode_pos.append((i, j))
        
        new_board = [['O'] * C for _ in range(R)]
        
        for x, y in explode_pos:
            new_board[x][y] = '.'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    new_board[nx][ny] = '.'
        
        return new_board

if N == 1:
    for row in grid:
        print(''.join(row))
elif N % 2 == 0:
    for _ in range(R):
        print('O' * C)
else:
    first_explode = explode(grid)
    second_explode = explode(first_explode)

    if N % 4 == 3:
        result = first_explode
    else:
        result = second_explode

    for row in result:
        print(''.join(row))
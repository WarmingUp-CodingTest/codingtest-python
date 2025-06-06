# 별 찍기 - 10
n = int(input())
board = [[' ' for _ in range(n)] for _ in range(n)]

def star(n, dx, dy, board):
    if n == 1:
        board[dx][dy] = '*'
        return

    size = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star(size, dx + i*size, dy + j * size, board)

star(n, 0, 0, board)
print('\n'.join(''.join(row) for row in board))
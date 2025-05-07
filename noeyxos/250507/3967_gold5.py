board = [list(input().strip()) for _ in range(5)]
positions = []
used = [False] * 13 

for i in range(5):
    for j in range(9):
        c = board[i][j]
        if c == 'x':
            positions.append((i, j))
        elif c != '.':
            used[ord(c) - ord('A') + 1] = True

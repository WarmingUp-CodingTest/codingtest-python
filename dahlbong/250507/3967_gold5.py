import sys
input = sys.stdin.readline

star_idx = [
    [(0, 4), (1, 3), (2, 2), (3, 1)],
    [(0, 4), (1, 5), (2, 6), (3, 7)],
    [(1, 1), (1, 3), (1, 5), (1, 7)],
    [(1, 1), (2, 2), (3, 3), (4, 4)],
    [(1, 7), (2, 6), (3, 5), (4, 4)],
    [(3, 1), (3, 3), (3, 5), (3, 7)],
]

inputs, empty = [], []
alphabets = [False] * 12

for i in range(5):
    row = list(input().rstrip())
    for j in range(9):
        if row[j] == 'x':
            empty.append((i, j))
        elif row[j] != '.':
            row[j] = ord(row[j]) - 65
            alphabets[row[j]] = True
    inputs.append(row)

def is_valid():
    for idx in star_idx:
        try:
            if sum(inputs[x][y] + 1 for x, y in idx) != 26:
                return False
        except:
            return False
    return True

def dfs(depth):
    if depth == len(empty):
        return is_valid()

    x, y = empty[depth]
    for i in range(12):
        if not alphabets[i]:
            # 재귀 돌리기
            return True
    return False

if dfs(0):
    for row in inputs:
        print(''.join(chr(c + 65) if isinstance(c, int) else c for c in row))

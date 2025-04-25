import sys
from collections import defaultdict
input = sys.stdin.readline

def is_bingo(board):
    bingos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    
    x_win = o_win = 0
    for idx1, idx2, idx3 in bingos:
        if board[idx1] == board[idx2] == board[idx3]:
            if board[idx1] == 'X':
                x_win += 1
            elif board[idx1] == 'O':
                o_win += 1
    
    if x_win and o_win: return 'both'
    elif x_win: return 'X'
    elif o_win: return 'O'
    return False

def tictactoe(board):
    flags = defaultdict(int)
    bingo = is_bingo(board)
    for b in board:
        flags[b] += 1

    if bingo == 'both': 
        return "invalid"
    elif bingo == 'O' and flags['O'] == flags['X']:
        return "valid"
    elif bingo == 'X' and flags['X'] == flags['O'] + 1:
        return "valid"
    elif not bingo and flags['X'] + flags['O'] == 9 and flags['X'] == flags['O'] + 1:
        return "valid"

    return "invalid"

boards = []
while True:
    inputs = input().rstrip()
    if inputs == "end":
        break
    boards.append(list(inputs))

for board in boards:
    print(tictactoe(board))

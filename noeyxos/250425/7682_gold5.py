def ticktacktoe(board):
    x_count = board.count('X')
    o_count = board.count('O')

    if o_count > x_count:
        return False

    if x_count - o_count not in [0, 1]:
        return False




while True:
    board = input()
    if board == 'end':
        break
    print("valid" if ticktacktoe(board) else "invalid")
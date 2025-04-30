import sys
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))
dir = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
sides, bottomTop = [0, 0, 0, 0], [0, 0]
cur = (x, y)

while moves:
    move = moves.pop(0)
    if 0 <= cur[0] + dir[move][0] < N and 0 <= cur[1] + dir[move][1] < M:
        cur = (cur[0] + dir[move][0], cur[1] + dir[move][1])
        if move == 1:
            tempTop, tempBottom = sides[1], sides[0]
            sides[0], sides[1] = bottomTop[1], bottomTop[0]
        elif move == 2:
            tempTop, tempBottom = sides[0], sides[1]
            sides[0], sides[1] = bottomTop[0], bottomTop[1]
        elif move == 3:
            tempTop, tempBottom = sides[2], sides[3]
            sides[2], sides[3] = bottomTop[0], bottomTop[1]
        elif move == 4:
            tempTop, tempBottom = sides[3], sides[2]
            sides[2], sides[3] = bottomTop[1], bottomTop[0]
        bottomTop = [tempBottom, tempTop]

        if board[cur[0]][cur[1]] != 0:
            bottomTop[0] = board[cur[0]][cur[1]]
            board[cur[0]][cur[1]] = 0
        else:
            board[cur[0]][cur[1]] = bottomTop[0]
        
        print(bottomTop[1])

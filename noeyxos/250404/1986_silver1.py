n, m = map(int, input().split())
chessboard = [[0] * m for _ in range(n)]

# 킹 퀸 폰 따로 리스트 만들기
queen = []
king = []
pawn = []

for position in [queen, king, pawn]:  
    data = list(map(int, input().split()))
    count = data[0]
    for i in range(count):
        x, y = data[i * 2 + 1] - 1, data[i * 2 + 2] - 1
        position.append((x, y))

# 현재 위치 저장
for x, y in queen:
    chessboard[x][y] = 1 
for x, y in king:
    chessboard[x][y] = 1 
for x, y in pawn:
    chessboard[x][y] = 1

def queen_attack():
    dx = [0, 1, 0, -1, -1, -1, 1, 1]
    dy = [1, 0, -1, 0, -1, 1, -1, 1]

    for x, y in queen:
        for d in range(8):
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                
                if not (0 <= nx < n and 0 <= ny < m):
                    break

                if (nx, ny) in queen or (nx, ny) in king or (nx, ny) in pawn:
                    break

                chessboard[nx][ny] = 1 



def king_attack():
def pawn_attack():
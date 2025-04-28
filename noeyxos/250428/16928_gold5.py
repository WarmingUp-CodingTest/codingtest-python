from collections import deque

n, m = map(int, input().split())

board = [0] * 101 

for _ in range(n): 
    x, y = map(int, input().split())
    board[x] = y


for _ in range(m): 
    u, v =  map(int, input().split())
    board[u] = v


def play_games(board):
    queue = deque([1])
    visited = [False] * 101
    visited[1] = True
    count = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()

            for dice in range(1, 7):
                next_pos = current + dice

                if next_pos > 100:
                    continue
                
                if board[next_pos] != 0:
                    next_pos = board[next_pos]

                if next_pos == 100:
                    return count +1

                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append(next_pos)

        count += 1

    return -1 
    
print(play_games(board))
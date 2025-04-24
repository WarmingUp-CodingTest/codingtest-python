from collections import deque

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
q = deque([[(0, 0), (0, 1)]])

def get_direction(start, end):
    row, col = end[0] - start[0], end[1] - start[1]
    if row == 0 and col == 1:
        return 'hori'
    elif row == 1 and col == 0:
        return 'vert'
    else:
        return 'diag'

def is_possible_route(ns, end, dx, dy):
    nex, ney = end[0] + dx, end[1] + dy
    if 0 <= nex < N and 0 <= ney < N:
        if dx == 1 and dy == 1:
            if home[nex][ney] == 0 and home[nex - 1][ney] == 0 and home[nex][ney - 1] == 0:
                q.append([ns, (nex, ney)])
        else:
            if home[nex][ney] == 0:
                q.append([ns, (nex, ney)])

while q:
    start, end = q.popleft()
    if end == (N - 1, N - 1):
        cnt += 1
        continue

    cur = get_direction(start, end)
    if cur == 'hori':
        ns = (start[0], start[1] + 1)
        is_possible_route(ns, end, 0, 1)
        is_possible_route(ns, end, 1, 1)

    elif cur == 'vert':
        ns = (start[0] + 1, start[1])
        is_possible_route(ns, end, 1, 0)
        is_possible_route(ns, end, 1, 1)

    elif cur == 'diag':
        ns = (start[0] + 1, start[1] + 1)
        is_possible_route(ns, end, 0, 1)
        is_possible_route(ns, end, 1, 0)
        is_possible_route(ns, end, 1, 1)

print(cnt)

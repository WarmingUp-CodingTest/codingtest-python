n,m,k = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(n)]

rotations = [tuple(map(int, input().split())) for _ in range(k)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


for rotation in rotations:
    r, c, s = rotation

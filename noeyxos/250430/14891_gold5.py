from collections import deque

gears = [(map(int, input())) for _ in range(4)]

k = int(input())
commands = [tuple(map(int, input().split())) for _ in range(k)]

score = 0

def rotate(idx, direction, visited):
    visited[idx] = True

    if idx > 0 and not visited[idx - 1]:
        if gears[idx][6] != gears[idx - 1][2]:
            rotate(idx - 1, -direction, visited)

    if idx < 3 and not visited[idx + 1]:
        if gears[idx][2] != gears[idx + 1][6]:
            rotate(idx + 1, -direction, visited)
    
    if direction == 1 :
        gears[idx].append(gears[idx].pop())
        
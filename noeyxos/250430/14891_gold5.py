from collections import deque

gears = [deque(map(int, input())) for _ in range(4)]

k = int(input())
commands = [tuple(map(int, input().split())) for _ in range(k)]

def rotate(idx, direction, visited):
    visited[idx] = True

    if idx > 0 and not visited[idx - 1]:
        if gears[idx][6] != gears[idx - 1][2]:
            rotate(idx - 1, -direction, visited)

    if idx < 3 and not visited[idx + 1]:
        if gears[idx][2] != gears[idx + 1][6]:
            rotate(idx + 1, -direction, visited)
    
    if direction == 1 :
        gears[idx].appendleft(gears[idx].pop())
    else : 
        gears[idx].append(gears[idx].popleft())


for gear_num, dir in commands:
    visited = [False] * 4
    rotate(gear_num - 1, dir, visited)
    
score = 0
for i in range(4): 
    if gears[i][0] == 1 : 
        score += (1 << i)


print(score)
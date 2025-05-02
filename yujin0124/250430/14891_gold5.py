from collections import deque
import sys
input = sys.stdin.readline

def rotate_gear(gear, direction):
    if direction == 1:
        gear.rotate(1)
    else:
        gear.rotate(-1)

def should_rotate(current, next, position):
    if position == 'left':
        return current[6] != next[2]
    else:
        return current[2] != next[6]

def propagate_rotation(gears, start, direction, visited):
    visited[start] = True
    current = gears[start]
    
    if start > 0 and not visited[start-1]:
        if should_rotate(current, gears[start-1], 'left'):
            propagate_rotation(gears, start-1, -direction, visited)
    
    if start < 3 and not visited[start+1]:
        if should_rotate(current, gears[start+1], 'right'):
            propagate_rotation(gears, start+1, -direction, visited)
    
    rotate_gear(current, direction)

def calculate_score(gears):
    score = 0
    for i in range(4):
        if gears[i][0] == 1: 
            score += (1 << i) 
    return score

gears = []
for _ in range(4):
    gear = deque(map(int, input().strip()))
    gears.append(gear)

k = int(input())
for _ in range(k):
    gear_num, direction = map(int, input().split())
    gear_idx = gear_num - 1 
    
    visited = [False] * 4
    propagate_rotation(gears, gear_idx, direction, visited)

score = calculate_score(gears)
print(score)
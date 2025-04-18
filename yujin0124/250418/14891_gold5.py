from collections import deque
import sys
input = sys.stdin.readline

def check_next_rotation_and_rotate(number, direction, visited):
    left, right = gears[number][6], gears[number][2]
    visited[number] = True
    rotate(number, direction)
    
    if number-1 > -1:
        if gears[number-1][2] != left and not visited[number-1]:
            check_next_rotation_and_rotate(number-1, direction * (-1), visited)
    if number+1 < 4:
        if gears[number+1][6] != right and not visited[number+1]:
            check_next_rotation_and_rotate(number+1, direction * (-1), visited)


def rotate(number, direction):
    if direction == 1:
        gears[number].rotate(1)
    else:
        gears[number].rotate(-1)

gears = []
for _ in range(4):
    temp = input().strip()
    gears.append(deque([int(i) for i in temp]))

k = int(input())
for _ in range(k):
    number, direction = map(int, input().split())
    visited = [False] * 4
    check_next_rotation_and_rotate(number-1, direction, visited)

score = 0
if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8
print(score)
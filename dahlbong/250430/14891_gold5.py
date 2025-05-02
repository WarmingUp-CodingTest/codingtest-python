from collections import deque
wheels = [deque(input().rstrip()) for _ in range(4)]
k = int(input())
rotates = [tuple(map(int, input().split())) for _ in range(k)]

def is_rotatable(wheels):
    rotatable = []
    for i in range(3):
        rotatable.append(wheels[i][2] != wheels[i+1][6])
    return rotatable

def rotate(wheel, dir):
    if dir == 1:
        wheel.appendleft(wheel.pop())
    else:
        wheel.append(wheel.popleft())

def rotate_wheels(wheels, start, dir):
    rotatable = is_rotatable(wheels)
    rotations = [0, 0, 0, 0]
    rotations[start-1] = dir

    for i in range(start-2, -1, -1):
        if rotatable[i]:
            rotations[i] = -rotations[i+1]
        else:
            break
    for i in range(start-1, 3):
        if rotatable[i]:
            rotations[i+1] = -rotations[i]
        else:
            break

    for i in range(4):
        if rotations[i] != 0:
            rotate(wheels[i], rotations[i])

for idx, dir in rotates:
    rotate_wheels(wheels, idx, dir)

score = 0
for i in range(4):
    if wheels[i][0] == '1':
        score += (1 << i)

print(score)

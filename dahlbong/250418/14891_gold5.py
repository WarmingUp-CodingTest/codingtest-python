import sys

input = sys.stdin.readline
wheels = [list(input().rstrip()) for _ in range(4)]
k = int(input())
rotates = [list(map(int, input().split())) for _ in range(k)]

def rotate_wheel(wheel, dir):
    if dir == 1:
        wheel.insert(0, wheel.pop())
    else:
        wheel.append(wheel.pop(0))

def check_left_neighbors(idx, dir):
    cur_dir = dir
    for i in range(idx -1, -1, -1):
        if wheels[i][2] != wheels[i+1][6]:
            cur_dir *= -1
            rotate_dir[i] = cur_dir
        else:
            break

def check_right_neighbors(idx, dir):
    cur_dir = dir
    for i in range(idx + 1, 4):
        if wheels[i - 1][2] != wheels[i][6]:
            cur_dir *= -1
            rotate_dir[i] = cur_dir
        else:
            break

for wheel_idx, dir in rotates:
    wheel_idx -= 1
    rotate_dir = [0] * 4
    rotate_dir[wheel_idx] = dir

    check_left_neighbors(wheel_idx, dir)
    check_right_neighbors(wheel_idx, dir)

    for i in range(4):
        if rotate_dir[i] != 0:
            rotate_wheel(wheels[i], rotate_dir[i])

score = 0
for i in range(4):
    if wheels[i][0] == '1':
        score += (1 << i)

print(score)
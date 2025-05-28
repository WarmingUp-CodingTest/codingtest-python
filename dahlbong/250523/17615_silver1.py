# 볼 모으기

import sys
input = sys.stdin.readline
N = int(input())
colors = list(input().rstrip())

def move_right(li, target_color):
    cnt = 0
    cur = li[-1]
    for i in range(N-1, -1, -1):
        if li[i] == target_color:
            if cur != target_color:
                cnt += 1       
        else:
            cur = li[i]
    return cnt

def move_left(li, target_color):
    cnt = 0
    cur = li[0]
    for i in range(N):
        if li[i] == target_color:
            if cur != target_color:
                cnt += 1       
        else:
            cur = li[i]
    return cnt

print(min(move_right(colors, 'R'), move_right(colors, 'B'),
            move_left(colors, 'R'), move_left(colors, 'B')))
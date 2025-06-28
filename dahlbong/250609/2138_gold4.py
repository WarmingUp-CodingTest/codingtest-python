# 전구와 스위치

import sys
input = sys.stdin.readline
N = int(input())
asis = list(input().rstrip())
tobe = list(input().rstrip())

def button(x, bulbs):
    for i in range(x-1, x+2):
        if 0 <= i < N:
            bulbs[i] = '1' if bulbs[i] == '0' else '0'

def sol(bulbs, start_with_pressing):
    bulbs = bulbs[:]
    cnt = 0

    if start_with_pressing:
        button(0, bulbs)
        cnt += 1

    for i in range(1, N):
        if bulbs[i-1] != tobe[i-1]:
            button(i, bulbs)
            cnt += 1
    
    return cnt if bulbs == tobe else float('inf')

ans = min(sol(asis, False), sol(asis, True))
print(ans if ans != float('inf') else -1)
import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))

def is_visible(a, b):
    if a + 1 == b:
        return True
    
    k = (buildings[b] - buildings[a]) / (b - a)
    for i in range(a+1, b):
        visible_height = buildings[a] + k * (i-a)
        if buildings[i] >= visible_height:
            return False
    return True

cnt = [0] * N

for i in range(N):
    for j in range(i):
        if is_visible(j, i):
            cnt[i] += 1
    for j in range(i+1, N):
        if is_visible(i, j):
            cnt[i] += 1

print(max(cnt))
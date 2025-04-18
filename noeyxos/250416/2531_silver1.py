import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]

sushi += sushi[:k-1]

cnt = {}
cnt[c] = 1

for i in range(k):
    if sushi[i] in cnt:
        cnt[sushi[i]] += 1
    else:
        cnt[sushi[i]] = 1

max_kind = len(cnt)

for i in range(1, n):
    left = sushi[i-1]
    cnt[left] -= 1
    if cnt[left] == 0:
        del cnt[left]

    right = sushi[i + k - 1]
    if right in cnt:
        cnt[right] += 1
    else:
        cnt[right] = 1

    max_kind = max(max_kind, len(cnt))

print(max_kind)
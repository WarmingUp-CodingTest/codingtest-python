import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi_belt = [int(input()) for _ in range(N)]
sushi_belt += sushi_belt[:k]

max_kind = 0

for i in range(N):
    current_sushi = sushi_belt[i:i+k]
    kinds = set(current_sushi)
    kinds.add(c)
    max_kind = max(max_kind, len(kinds))

print(max_kind)
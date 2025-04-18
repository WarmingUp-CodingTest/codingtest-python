import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    x, y = map(int, input().split())
    lines.append([x, y])

lines.sort()

start, end = lines[0]
result = 0

for i in range(1, n):
    x, y = lines[i]
    
    if x <= end:
        end = max(y, end)
    else:
        result += end - start
        start = x
        end = y

result += end - start
print(result)
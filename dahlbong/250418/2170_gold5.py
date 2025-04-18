import sys
input = sys.stdin.readline
lines = []
total = 0
for i in range(int(input())):
    lines.append(tuple(map(int, input().split())))
lines.sort(key = lambda x : (x[0], -x[1]))

cur_point = lines[0][0]
for start, end in lines:
    if cur_point > end:
        continue

    if start > cur_point:
        cur_point = start
    total += end - cur_point
    cur_point = end

print(total)

import sys
input = sys.stdin.readline

k, n = map(int, input().split())

start = 1
end = -1
lines = []
for i in range(k):
    line = int(input())
    lines.append(line)
    end = max(end, line)

while start <= end:
    mid = (start + end) // 2
    
    cut_count = 0
    for line in lines:
        cut_count += line // mid
    
    if cut_count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
import sys
input = sys.stdin.readline

n = int(input())
properties = list(map(int, input().split()))

x, start = 0, 0
y, end = n - 1, n - 1
result = properties[y] + properties[x]


while x < y:
    diff = properties[y] + properties[x]
    
    if diff == 0:
        start = x
        end = y
        break
    
    if abs(diff) < abs(result):
        result = diff
        start = x
        end = y
    
    if diff > 0:
        y -= 1
    else:
        x += 1

print(properties[start], properties[end])
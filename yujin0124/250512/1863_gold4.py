import sys
input = sys.stdin.readline

n = int(input())
buildings = []
for _ in range(n):
    x, y = map(int, input().split())
    buildings.append(y)
buildings.append(0)

result = 0
stack = [0]
for building in buildings:
    temp = building
    while stack[-1] > building:
        if stack[-1] != temp:
            result += 1
            temp = stack[-1]
        stack.pop()
    stack.append(building)

print(result)
import sys
input = sys.stdin.readline

n = int(input())
balls = input().strip()

temp = balls[0]
start = 0 if temp == 'R' else 1
s = 0
number = []
for ball in balls:
  if temp != ball:
    number.append(s)
    s = 0
    temp = ball
  s += 1
number.append(s)

first = sum(number[::2])
second = sum(number[1::2])

if len(number) % 2 == 1:
  first -= max(number[0], number[-1])
else:
  first -= number[0]
  second -= number[-1]

print(min(first, second))
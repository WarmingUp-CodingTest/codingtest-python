import sys
input = sys.stdin.readline

n, k = map(int, input().split())
belts = list(map(int, input().split()))
step = 0
robots = [False] * (2*n)

def move():
  belts.insert(0, belts.pop())
  robots.insert(0, robots.pop())
  robots[n-1] = False

def move_robot():
  for i in range(n-2, -1, -1):
    if robots[i] and not robots[i+1] and belts[i+1] > 0:
      robots[i] = False
      robots[i+1] = True
      belts[i+1] -= 1
  robots[n-1] = False

def put_robot():
  if belts[0] > 0:
    robots[0] = True
    belts[0] -= 1

def check():
  return belts.count(0) >= k

while True:
  step += 1
  move()
  move_robot()
  put_robot()
  if check():
    break

print(step)
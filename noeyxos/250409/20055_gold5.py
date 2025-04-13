import sys
input = sys.stdin.readline

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False] * n

step = 0 

while True:
    step += 1

    belt = [belt[-1]] + belt[:-1]
    robot = [False] + robot[:-1]
    robot[n-1] = False

    for i in range(n-2, -1, -1) : 
        if robot[i] and not robot[i+1] and belt[i+1] > 0: 
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
    robot[n-1] = False

    if belt[0] > 0 : 
        robot[0] = True
        belt[0] -= 1

    if belt.count(0) >= k:
        break
print(step)
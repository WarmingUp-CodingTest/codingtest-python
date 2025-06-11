import sys
input = sys.stdin.readline

N = int(input())

dices = [list(map(int, input().split())) for _ in range(N)]

sides = {
  0:5, 1:3, 2:4, 3:1, 4:2, 5:0
}

result = 0
for i in range(1, 7):
  max_sum = 0
  bottom = i
  for j in range(N):
    for k in range(6):
      if dices[j][k] == bottom:
        top = dices[j][sides[k]]
        if bottom != 6 and top != 6:
          max_sum += 6
        elif bottom != 5 and top != 5:
          max_sum += 5
        else:
          max_sum += 4    
        bottom = top
        break
  
  if result < max_sum:
    result = max_sum

print(result)
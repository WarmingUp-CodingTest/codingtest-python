k = int(input())
arr = list(input().split())

used = [False] * 10
numbers = []
result = []

def check(ineq, x, y):
  return x > y if ineq == '>' else x < y

def back(depth):
  if depth >= k+1:
    result.append("".join(map(str, numbers)))
    return
  
  for i in range(10):
    if used[i]:
      continue
    
    if depth == 0 or check(arr[depth-1], numbers[depth-1], i):
      used[i] = True
      numbers.append(i)
      back(depth+1)
      numbers.pop()
      used[i] = False

back(0)
result.sort()
print(result[-1])
print(result[0])
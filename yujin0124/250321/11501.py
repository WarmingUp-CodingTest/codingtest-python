t = int(input())

while t:
  t -= 1
  n = int(input())
  stocks = list(map(int, input().split()))
  
  max = stocks[n-1]
  sum = 0
  for i in range(n-2, -1, -1):
    if stocks[i] < max:
      sum += max - stocks[i]
    elif stocks[i] > max:
      max = stocks[i]
  
  print(sum)
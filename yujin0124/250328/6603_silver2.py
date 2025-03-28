def back(n, x):
  if n == 6:
    for i in result:
      print(i, end=" ")
    print()
    return
  
  for i in range(x, k):
    result[n] = arr[i+1]
    back(n+1, i+1)

while True:
  arr = list(map(int, input().split()))
  k = arr[0]
  if k == 0:
    break
  
  result = [0] * 6
  back(0, 0)
  print()
  
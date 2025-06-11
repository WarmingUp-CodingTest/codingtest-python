N = int(input())

current = [int(i) for i in input().strip()]
want = [int(i) for i in input().strip()]

result =[]
for first in [True, False]:
  current_temp = current.copy()
  count = 0
  
  if first:
    current_temp[0] ^= 1
    current_temp[1] ^= 1
    count += 1
  
  for i in range(1, N):
    if current_temp[i-1] != want[i-1]:
      current_temp[i-1] ^= 1
      current_temp[i] ^= 1
      if i+1 < N:
        current_temp[i+1] ^= 1
      count += 1
  if current_temp == want:
    result.append(count)

if result:
  print(min(result))
else:
  print("-1")
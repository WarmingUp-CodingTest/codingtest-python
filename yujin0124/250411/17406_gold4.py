from itertools import permutations

def rotate(arr, r, c, s):
  result = [row[:] for row in arr]
  
  for i in range(1, s+1):
    temp = result[r-i][c-i]

    for j in range(r-i, r+i):
      result[j][c-i] = result[j+1][c-i]

    for j in range(c-i, c+i):
      result[r+i][j] = result[r+i][j+1]

    for j in range(r+i, r-i, -1):
      result[j][c+i] = result[j-1][c+i]

    for j in range(c+i, c-i, -1):
      result[r-i][j] = result[r-i][j-1]

    result[r-i][c-i+1] = temp
  return result

def calculate_array_value(arr):
  return min(sum(row) for row in arr)

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

operations = []
for i in range(k):
  r, c, s = map(int, input().split())
  operations.append((r-1, c-1, s))

result = float('inf')

for perm in permutations(operations):
  temp_arr = [row[:] for row in arr]
  for r, c, s in perm:
    temp_arr = rotate(temp_arr, r, c, s)
  
  current = calculate_array_value(temp_arr)
  
  result = min(result, current)

print(result)
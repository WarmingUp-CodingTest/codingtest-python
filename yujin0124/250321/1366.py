def diff(n, m) -> int:
  if n > m:
    return diff(m, n)
  
  diff1 = m - n
  diff2 = n - m + 12
  
  return diff1 if diff1 < diff2 else diff2

def transform(arr) -> list:
  transformed_arr = []
  
  for i in range(len(arr)):
    for j, note in enumerate(notes):
      if note == arr[i]:
        transformed_arr.append(j)
        
  return transformed_arr

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
n, m = map(int, input().split())
strings = list(input().split())
codes = list(input().split())

strings_number = transform(strings)
codes_number = transform(codes)

frets = []
for string in strings_number:
  diff_min = 15
  for code in codes_number:
    temp = diff(string, code)
    if diff_min > temp:
      diff_min = temp
    print(temp) 
  
min = 15
max = -1
for fret in frets:
  if fret == 0:
    continue
  if fret < min:
    min = fret
  if fret > max:
    max = fret

result = 0
if min == 15 and max == -1:
  result = 0
elif min == 15 or max == -1:
  result = 1
else:
  result = max - min + 1

print(result)
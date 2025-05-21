G = int(input())

answer = []

start = 1
end = 2
while True:
  
  if end ** 2 - (end-1) ** 2 > 100_000:
    break
  
  if end ** 2 - start ** 2 > G:
    start += 1
    continue
  
  if end ** 2 - start  ** 2 < G:
    end += 1
    continue
  
  answer.append(end)
  end += 1

if answer:
  print(*answer, sep='\n')
else:
  print("-1")
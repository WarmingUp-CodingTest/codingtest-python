def recursion(n):
  if n == 1:
    return ["*"]
  
  star = recursion(n//3)
  stars = []
  for s in star:
    stars.append(s*3)
  for s in star:
    stars.append(s + " " * (n//3) + s)
  for s in star:
    stars.append(s*3)
  
  return stars

N = int(input())
stars = recursion(N)
for star in stars:
  print(star)
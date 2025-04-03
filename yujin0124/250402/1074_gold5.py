import sys
sys.setrecursionlimit(10**6)

def z(x, y, n):
  if n == 0:
    return 0
  
  half = 2 ** (n-1)
  
  if x < half and y < half:
    return z(x, y, n-1)
  elif x < half and y >= half:
    return half*half + z(x, y-half, n-1)
  elif x >= half and y < half:
    return 2*half*half + z(x-half, y, n-1)
  else:
    return 3*half*half + z(x-half, y-half, n-1)

n, r, c = map(int, input().split())
print(z(r, c, n))
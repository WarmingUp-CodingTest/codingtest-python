import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def root(arr, x):
  if arr[x] != x:
    arr[x] = root(arr, arr[x])
  return arr[x]
  

n, m = map(int, input().split())
arr = [i for i in range(n+1)]

for i in range(m):
  operator, a, b = map(int, input().split())
  
  if operator == 0:
    a = root(arr, a)
    b = root(arr, b)
    if a < b:
      arr[b] = a
    else:
      arr[a] = b
  else:
    if root(arr, a) == root(arr, b):
      print("YES")
    else:
      print("NO")
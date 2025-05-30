import sys
input = sys.stdin.readline

def find(arr, x):
  if arr[x] != x:
    arr[x] = find(arr, arr[x])
  return arr[x]

def union(arr, a, b):
  a_parent = find(arr, a)
  b_parent = find(arr, b)
  
  if a_parent < b_parent:
    arr[b_parent] = a_parent
  else:
    arr[a_parent] = b_parent


N = int(input())
M = int(input())
parents = [i for i in range(N+1)]
for i in range(1, N+1):
  temp = list(map(int, input().split()))
  for j in range(1, N+1):
    if temp[j-1] == 1:
      union(parents, i, j)

routes = list(map(int, input().split()))
result = True
for i in range(M-1):
  if find(parents, routes[i]) != find(parents, routes[i+1]):
    result = False
    break

print("YES" if result else "NO")
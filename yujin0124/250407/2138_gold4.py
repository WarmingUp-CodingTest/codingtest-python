import sys
input = sys.stdin.readline

def solution(n, current, target):
  result =[]
  for first in [True, False]:
    state = current.copy()
    count = 0
    
    if first:
      state[0] ^= 1
      state[1] ^= 1
      count += 1
    
    for i in range(1, n):
      if state[i-1] != target[i-1]:
        state[i-1] ^= 1
        state[i] ^= 1
        if i+1 < n:
          state[i+1] ^= 1
        count += 1
    if state == target:
      result.append(count)
  if result:
    return min(result)
  return -1

n = int(input())
current = [int(i) for i in input().strip()]
target = [int(i) for i in input().strip()]

print(solution(n, current, target))
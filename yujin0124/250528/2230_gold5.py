import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = sorted(arr)

start = 0
end = 1
result = int(2e9)

while start < N and end < N:
  temp = arr[end] - arr[start]
  if M > temp:
    end += 1
    continue
  if M < temp:
    if temp < result:
      result = temp
    start += 1
    continue
  result = M
  break

print(result)    
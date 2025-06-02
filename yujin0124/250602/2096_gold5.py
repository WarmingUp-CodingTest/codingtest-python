import sys
input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().split())
dp_small = [a, b, c]
dp_big = [a, b, c]
temp_small = [0] * 3
temp_big = [0] * 3

for i in range(1, N):
  a, b, c = map(int, input().split())
  
  for j in range(3):
    temp_small[j] = dp_small[j]
    temp_big[j] = dp_big[j]
  
  dp_small[0] = a + min(temp_small[0], temp_small[1])
  dp_small[1] = b + min(temp_small[0], temp_small[1], temp_small[2])
  dp_small[2] = c + min(temp_small[1], temp_small[2])
  
  dp_big[0] = a + max(temp_big[0], temp_big[1])
  dp_big[1] = b + max(temp_big[0], temp_big[1], temp_big[2])
  dp_big[2] = c + max(temp_big[1], temp_big[2])
  
print(max(dp_big[i] for i in range(3)), min(dp_small[i] for i in range(3)))
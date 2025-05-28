import sys
input = sys.stdin.readline

def can_fold(fold_information):
  if len(fold_information) == 1:
    return True
  
  for i in range(len(fold_information) // 2):
    if fold_information[i] == fold_information[-1 * i + -1]:
      return False
  return can_fold(fold_information[:len(fold_information) // 2])

T = int(input())
while T:
  T -= 1

  fold_information = input().strip()
  result = can_fold(fold_information)
  print("YES" if result else "NO")
  
#1802 종이접기
import sys
input = sys.stdin.readline

def foldable(command):
    if len(command) == 1:
        return True
        
    mid = len(command) // 2
    left, right = command[:mid], command[mid+1:]
    if left != [x ^ 1 for x in reversed(right)]:
        return False
        
    return foldable(left) and foldable(right)
    

for _ in range(int(input())):
    command = list(map(int, input().strip()))
    print('YES' if foldable(command) else 'NO')
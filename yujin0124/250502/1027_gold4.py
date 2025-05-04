import sys
input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))
result = 0

for i in range(n):
    visible = n - 1
    
    for j in range(0, i):
        for k in range(j+1, i):
            if (buildings[k] - buildings[j]) * (i-j) >= (buildings[i] - buildings[j]) * (k-j):
                visible -= 1
                break
    
    for j in range(i+1, n):
        for k in range(i+1, j):
            if (buildings[k] - buildings[i]) * (j-i) >= (buildings[j] - buildings[i]) * (k-i):
                visible -= 1
                break
            
    result = max(visible, result)

print(result)
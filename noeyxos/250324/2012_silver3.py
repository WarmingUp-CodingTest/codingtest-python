import sys

input = sys.stdin.readline

n = int(input())
rank = sorted([int(input()) for _ in range(n)])
dissatisfaction = sum(abs(rank[i] - (i+1)) for i in range(n))

print(dissatisfaction)
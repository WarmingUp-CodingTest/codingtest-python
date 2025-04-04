import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

dp = [0] * n

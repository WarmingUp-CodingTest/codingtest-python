#1715 카드 정렬하기
import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = list(int(input()) for _ in range(n))
temp = 0

heapq.heapify(q)

while len(q) != 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a + b)
    temp += a + b

print(temp)
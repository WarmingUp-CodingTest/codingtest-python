import sys
input = sys.stdin.readline

n = int(input())
estimated_ranks = [0] * (n+1)
for i in range(n):
  estimated_ranks[i+1] = int(input())

estimated_ranks.sort()
complaint = 0
for real_rank, estimated_rank in enumerate(estimated_ranks):
  complaint += abs(estimated_rank - real_rank)

print(complaint)
  
from itertools import permutations
import sys
input = sys.stdin.readline

def calculate_min_sum(graph):
    return min(sum(row) for row in graph)

def rotate(graph, r, c, s):
    
    return


N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
calc = [tuple(map(int, input().split())) for _ in range(K)]

min_value = float('inf')
for perm in permutations(calc):
    graph = [row[:] for row in graph]
    for r, c, s in perm:
        rotate(graph, r - 1, c - 1, s)
    min_value = min(min_value, calculate_min_sum(graph))

print(min_value)

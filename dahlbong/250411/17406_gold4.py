from itertools import permutations
import sys
input = sys.stdin.readline

def calculate_min_sum(graph):
    return min(sum(row) for row in graph)

def rotate(graph, r, c, s):
    for layer in range(1, s + 1):
        top = r - layer
        left = c - layer
        bottom = r + layer
        right = c + layer

        prev = graph[top][left]

        for j in range(left + 1, right + 1):
            graph[top][j], prev = prev, graph[top][j]
        for i in range(top + 1, bottom + 1):
            graph[i][right], prev = prev, graph[i][right]
        for j in range(right - 1, left - 1, -1):
            graph[bottom][j], prev = prev, graph[bottom][j]
        for i in range(bottom - 1, top - 1, -1):
            graph[i][left], prev = prev, graph[i][left]


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

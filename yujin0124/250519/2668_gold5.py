import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(current, path):
    path.add(current)
    visited[current] = 1
    for next_num in graph[current]:
        if next_num not in path:
            dfs(next_num, path.copy())
        else:
            selected_numbers.extend(list(path))
            return

n = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for i in range(1, n+1):
    number = int(sys.stdin.readline().strip())
    graph[number].append(i)

visited = [0 for _ in range(n+1)]
selected_numbers = []
for i in range(1, n+1):
    if not visited[i]:
        dfs(i, set([]))

selected_numbers.sort()
print(len(selected_numbers))
for num in selected_numbers:
    print(num)
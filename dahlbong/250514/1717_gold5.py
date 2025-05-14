import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(m):
    check_ans, a, b = map(int, input().split())
    if not check_ans:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
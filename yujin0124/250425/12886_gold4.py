def sol(A, B, C):
    total = A + B + C
    if total % 3 != 0:
        return 0

A, B, C = map(int, input().split())
print(sol(A, B, C))

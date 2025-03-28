from itertools import combinations

while True:

    S = list(map(int, input().split()))
    k = S.pop(0)

    if k == 0:
        break

    for l in list(combinations(S, 6)):
        print(*l)

    print()
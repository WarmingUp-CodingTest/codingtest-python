from itertools import combinations


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []


for i in range(n): 
    for j in range(n): 
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2: 
            chicken.append((i, j))

def chicken_distance(a, b): 
    return abs(a[0]- b[0]) + abs(a[1]-b[1])


ans = 2 * n * len(house)

for combi in combinations(chicken, m): 
    total = 0

    for hou in house :
        closest_distance = float('inf')
        for chi in combi : 
            dist = chicken_distance(hou, chi)
            closest_distance = min(closest_distance, dist)   

        total += closest_distance
    
    ans = min(ans, total)

print(ans)
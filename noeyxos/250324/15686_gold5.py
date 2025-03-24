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

print(house)
print(chicken)

def chicken_distance(a, b): 
    return abs(a[0]- b[0]) + abs(a[1]-b[1])


# for dx, dy in city :
#     min_distance = 
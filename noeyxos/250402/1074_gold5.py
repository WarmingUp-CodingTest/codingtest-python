N, r, c = map(int, input().split())

size = 2 ** N
x, y = 0, 0
count = 0


while size > 0 :
    size //= 2

    if r < x + size and c < y + size :
        pass
    elif r < x + size and c >= y + size: 
        count += size * size
        y += size
    elif r >= x + size and c < y + size:
        count += 2 * size * size
        x += size
    else:
        count += 3 * size * size
        x += size
        y += size

print(count)
h, w = map(int, input().split())
maps = list(map(int, input().split()))

if w <= 2:
    print(0)
    exit(0)

left, right = 0, w - 1
left_max, right_max = 0, 0
total_water = 0

while left < right:
    if maps[left] < maps[right]:
        if maps[left] >= left_max:
            left_max = maps[left]
        else:
            total_water += left_max - maps[left]
        left += 1
    else:
        if maps[right] >= right_max:
            right_max = maps[right]
        else:
            total_water += right_max - maps[right]
        right -= 1

print(total_water)
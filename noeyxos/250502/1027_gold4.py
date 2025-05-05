n = int(input())
height = list(map(int, input().split()))

def visible_buildings():
    max_visible = 0

    for i in range(n):
        count = 0
        max_slope_left = float('-inf')
        max_slope_right = float('-inf')

        for j in range(i - 1, -1, -1):
            slope = (height[i] - height[j]) / (i - j)
            if slope > max_slope_left:
                max_slope_left = slope
                count += 1

        for j in range(i + 1, n):
            slope = (height[j] - height[i]) / (j - i)
            if slope > max_slope_right:
                max_slope_right = slope
                count += 1

        max_visible = max(max_visible, count)

    return max_visible

print(visible_buildings())
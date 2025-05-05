import sys

N = int(sys.stdin.readline())
liquid_values = list(map(int, sys.stdin.readline().split()))


def solve(values):
    values.sort()
    
    left = 0
    right = len(values) - 1

    min_diff = float('inf')
    result = (0, 0)

    while left < right:
        mix = values[left] + values[right]

        if abs(mix) < min_diff:
            min_diff = abs(mix)
            result = (values[left], values[right])
        
        if mix < 0:
            left += 1
        else:
            right -= 1

    return result

a, b = solve(liquid_values)
print(a, b)
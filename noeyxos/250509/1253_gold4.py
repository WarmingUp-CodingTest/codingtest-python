N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for i in range(N):
    target = A[i]
    left = 0
    right = N - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        temp_sum = A[left] + A[right]
        if temp_sum == target:
            count += 1
            break
        elif temp_sum < target:
            left += 1
        else:
            right -= 1

print(count)
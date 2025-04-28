def swap_words(s):
    n = len(s)
    b_count = s.count('b')

    if b_count == 0 or b_count == n:
        return 0

    b_group = s[:b_count]
    min_changes = b_group.count('a')

    current_changes = min_changes

    for i in range(1, n):
        out_idx = i - 1
        in_idx = (i + b_count - 1) % n

        if s[out_idx] == 'a':
            current_changes -= 1
        if s[in_idx] == 'a':
            current_changes += 1

        min_changes = min(min_changes, current_changes)

    return min_changes

s = input().strip()
print(swap_words(s))
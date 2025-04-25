from collections import deque

a, b, c = map(int, input().split())

def move_equals(a, b, c): 
    total = a + b + c
    if total % 3 != 0: 
        return 0

    queue = deque()
    visited = set()

    initial = tuple(sorted((a, b, c)))
    queue.append(initial)
    visited.add(initial)

    while queue: 
        x, y, z = queue.popleft() 

        if x == y == z: 
            return 1 
        
        for i, j in [(x, y), (x, z), (y, z)]:
            if i != j:
                small_group = min(i, j)
                large_group = max(i, j)

                new_small = small_group * 2
                new_large = large_group - small_group
                remain = total - new_small - new_large

                new_state = tuple(sorted((new_small, new_large, remain)))

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)

    return 0

print(move_equals(a, b, c))
def sol(s):
    n = len(s)
    a_count = s.count('a')
    
    if a_count == 0 or a_count == n:
        return 0
    
    min_swap = float('inf')
    
    for i in range(n): 
        swap = 0
        for j in range(i, i + a_count):
            if s[j % n] == 'b':
                swap += 1
        
        min_swap = min(min_swap, swap)
    
    return min_swap

s = input().strip()
print(sol(s))
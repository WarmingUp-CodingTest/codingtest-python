import sys
sys.setrecursionlimit(10**6)

n, r, c = map(int, sys.stdin.readline().split())
ans = 0

def quarterize(x, y, size):
    global ans
    new_size = size // 2

    if size == 1:
        print(ans)
        return
    
    if x <= r < x + new_size and y <= c < y + new_size:
        quarterize(x, y, new_size)
    elif x <= r < x + new_size and y + new_size <= c < y + 2*new_size:
        ans += new_size**2
        quarterize(x, y+new_size, new_size)
    elif x + new_size <= r < x + 2*new_size and y <= c < y + new_size:
        ans += 2 * (new_size**2)
        quarterize(x+new_size, y, new_size)
    else:
        ans += 3 * (new_size**2)
        quarterize(x+new_size, y+new_size, new_size)

quarterize(0, 0, 2**n)

def sol(s, t):
    if s == t:
        return True
    
    if len(t) < len(s):
        return False
    
    if t[-1] == 'A' and sol(s, t[:-1]):
        return True
    
    t_reversed = t[::-1]
    if t_reversed[-1] == 'B' and sol(s, t_reversed[:-1]):
        return True
    
    return False

s = input().strip()
t = input().strip()

if sol(s, t):
    print("1")
else:
    print("0")
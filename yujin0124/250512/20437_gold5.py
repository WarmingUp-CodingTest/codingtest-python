import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    str = input().strip()
    n = int(input())
    dict = {}
    
    for index, cha in enumerate(str):
        if str.count(cha) >= n:
            if cha not in dict:
                dict[cha] = []
            dict[cha].append(index)
    
    if not dict:
        print(-1)
    else:
        short_len = 100000
        long_len = 0
        for cha in dict:
            for i in range(len(dict[cha])-n+1):
                temp = dict[cha][i+n-1] - dict[cha][i] + 1
                short_len = min(short_len, temp)
                long_len = max(long_len, temp)
        print(short_len, long_len)
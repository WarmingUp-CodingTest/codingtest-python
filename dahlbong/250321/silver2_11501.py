import sys
from collections import deque
input = sys.stdin.readline

def sol():
    N = int(input())
    stocks = deque(list(map(int, input().split())))
    gain = 0
    max_price = 0
    # max_stock = max(stocks)
    # while stocks:
    #     cur_stock = stocks.popleft()

    #     if cur_stock < max_stock:
    #         gain += max_stock - cur_stock
    #     else:
    #         max_stock = max(stocks) if stocks else 0
    
    for i in range(N-1, -1, -1):
        if stocks[i] > max_price:
            max_price = stocks[i]
        else:
            gain += max_price - stocks[i]
    
    return gain

T = int(input())
for _ in range(T):
    print(sol())
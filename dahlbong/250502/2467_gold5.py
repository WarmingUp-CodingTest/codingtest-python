import sys
input = sys.stdin.readline
N = int(input())
liquids = list(map(int, input().split()))

def get_ans():
    if liquids[0] > 0:
        print(liquids[0], liquids[1])
        return
    elif liquids[-1] < 0:
        print(liquids[-2], liquids[-1])
        return
    else:
        left, right = search()
        print(left, right)
        return
    
def search():
    min_sum = float('inf')
    left, right = 0, N-1
    result = (liquids[left], liquids[right])

    while left < right:
        cur_sum = liquids[left] + liquids[right]
        if abs(cur_sum) < abs(min_sum):
            min_sum = cur_sum
            result = (liquids[left], liquids[right])
        if cur_sum < 0:
            left += 1
        else:
            right -= 1
    
    return result

get_ans()
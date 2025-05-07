import sys
input = sys.stdin.readline

def calculate_expression(expression):
    num = 0
    sign = 1
    current_number = 0
    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '+' or char == '-':
            num += sign * current_number
            current_number = 0
            sign = 1 if char == '+' else -1
    num += sign * current_number
    return num

def make_expression(n, current, idx, result):
    if idx == n:
        temp = current.replace(" ", "")
        if calculate_expression(temp) == 0:
            result.append(current)
        return

    next_num = str(idx + 1)
    make_expression(n, current + " " + next_num, idx + 1, result)
    make_expression(n, current + "+" + next_num, idx + 1, result)
    make_expression(n, current + "-" + next_num, idx + 1, result)

T = int(input())
for _ in range(T):
    N = int(input())
    result = []
    make_expression(N, "1", 1, result)
    for expr in result:
        print(expr)
    print()
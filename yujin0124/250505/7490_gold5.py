from itertools import product

arr = [' ', '+', '-']

def calculation(mark, numbers):
    new_numbers = []
    current_number = str(numbers[0])

    for i in range(len(mark)):
        if mark[i] == ' ':
            current_number += str(numbers[i+1])
        else:
            new_numbers.append(int(current_number))
            current_number = str(numbers[i+1])
    new_numbers.append(int(current_number))
    
    result = new_numbers[0]
    index = 0
    
    for i in range(1, len(new_numbers)):
        while index < len(mark) and mark[index] == ' ':
            index += 1
        
        if index < len(mark):
            if mark[index] == '+':
                result += new_numbers[i]  
            else:
                result -= new_numbers[i]
            index += 1
    
    return result

def print_result(mark, numbers):
    for i, x in enumerate(numbers):
        print(x, end="")
        if i < len(mark):
            print(mark[i], end="")
    print()

t = int(input())
for case in range(t):
    n = int(input())
    
    marks = product(arr, repeat=n-1)
    numbers = list(i for i in range(1, n+1))
    
    for mark in marks:
        if calculation(mark, numbers) == 0:
            print_result(mark, numbers)
    
    if case < t - 1:
        print()
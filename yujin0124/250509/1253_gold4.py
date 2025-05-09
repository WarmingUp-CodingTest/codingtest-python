import sys
input = sys.stdin.readline

n =int(input().strip())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
result = 0

for index, number in enumerate(numbers):
    temp = numbers[:index] + numbers[index+1:]
    
    start, end = 0, n-2
    
    while start < end:
        current = temp[start] + temp[end]
        
        if current == number:
            result += 1
            break
        
        if current < number:
            start += 1
        else:
            end -= 1

print(result)
n = int(input())

circum = list(map(int, input().strip()))
target = list(map(int, input().strip()))

def press_switch(bulbs, i): 
    for idx in range(i-1, i+2): 
        if 0 <= idx < len(bulbs):
            bulbs[idx] = 1 - bulbs[idx]

def turn_on(circum, target, first_press): 
    bulbs = circum[:]
    count = 0 

    if first_press: 
        press_switch(bulbs, 0)
        count += 1

    for i in range(1, len(bulbs)): 
        if bulbs[i-1] != target[i-1]:
            press_switch(bulbs, i)
            count += 1

    return count if bulbs == target else float('inf')


res = min(turn_on(circum, target, True), turn_on(circum, target, False))
print(res if res != float('inf') else -1)
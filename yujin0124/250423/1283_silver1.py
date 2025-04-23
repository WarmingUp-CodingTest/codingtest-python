used = set()
result = []

n = int(input())
strs = []

for i in range(n):
    strs.append(input().strip())

for str in strs:
    
    check = False
    splited = str.split(" ")
    for i, word in enumerate(splited):
        first_char = word[0].upper()
        if first_char not in used:
            used.add(first_char)
            splited[i] = f"[{word[0]}]{word[1:]}"
            check = True
            break
    
    if not check:
        for i, word in enumerate(splited):
            for j, char in enumerate(word):
                if j == 0:
                    continue
                
                if char.upper() not in used:
                    used.add(char.upper())
                    splited[i] = f"{word[:j]}[{char}]{word[j+1:]}"
                    check = True
                    break
                    
            if check:
                break
    
    result.append(' '.join(splited))

for i in result:
    print(i)
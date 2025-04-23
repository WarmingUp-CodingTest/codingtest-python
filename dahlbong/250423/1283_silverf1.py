N = int(input())
options = [input().split() for _ in range(N)]
keys = []

for option in options:
    got_key = False
    for i in range(len(option)):
        if option[i][0].lower() not in keys:
            keys.append(option[i][0].lower())
            option[i] = '[' + option[i][0] + ']' + option[i][1:]
            got_key = True
            break
    
    if not got_key:
        for i in range(len(option)):
            word = option[i]
            for j in range(1, len(word)):
                if word[j].lower() not in keys:
                    keys.append(word[j].lower())
                    option[i] = word[:j] + '[' + word[j] + ']' + word[j+1:]
                    got_key = True
                    break
            if got_key:
                break

for o in options:
    print(' '.join(o))
    
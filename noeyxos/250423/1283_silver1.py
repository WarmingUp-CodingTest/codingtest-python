n = int(input())
options = [input() for _ in range(n)]

shortcuts = []

def set_shortcut(phrase):
    words = phrase.split()

    for i in range(len(words)):
        ch = words[i][0].lower()
        if ch not in shortcuts:
            shortcuts.append(ch)
            words[i] = f"[{words[i][0]}]{words[i][1:]}"
            return ' '.join(words)

    for i in range(len(phrase)):
        ch = phrase[i].lower()
        if ch != ' ' and ch not in shortcuts:
            shortcuts.append(ch)
            return phrase[:i] + f"[{phrase[i]}]" + phrase[i+1:]

    return phrase

for option in options:
    print(set_shortcut(option))
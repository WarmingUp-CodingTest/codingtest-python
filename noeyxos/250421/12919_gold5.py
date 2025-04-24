s = input()
t = input()

found = False

def make_word(current):
    global found

    if found:
        return

    if current == s:
        found = True
        return

    if len(current) < len(s):
        return

    if current[-1] == 'A':
        make_word(current[:-1])
    
    if current[0] == 'B':
        make_word(current[1:][::-1])

make_word(t)
print(1 if found else 0)
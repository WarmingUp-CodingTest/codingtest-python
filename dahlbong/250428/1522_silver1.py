sentence = input().rstrip()
cnt_a = sentence.count('a') 
cnt_b = sentence[:cnt_a].count('b')
min_b = cnt_b
sentence += sentence 

for i in range(1, len(sentence) // 2):
    if sentence[i-1] == 'b':
        cnt_b -= 1
    if sentence[i+cnt_a-1] == 'b':
        cnt_b += 1
    min_b = min(min_b, cnt_b)

print(min_b)

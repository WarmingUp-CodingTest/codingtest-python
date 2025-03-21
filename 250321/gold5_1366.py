note = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
N, M = map(int, input().split())
guitar = list(input().split())
chord = list(input().split())
guitar_idx = []
frets = []

for g in guitar:
    cur_fret = []
    for c in chord:
        chord_idx = note.index(c)
        if chord_idx == note.index(g):
            cur_fret.append(0)
        else:
            cur_fret.append((chord_idx - note.index(g)) % 12)
    frets.append(cur_fret)

print(frets)

checked = [False] * N
fret_candidates = [list(x) for x in zip(*frets)]
final_fret = []

for i in range(M):
    final_fret.append(min(fret_candidates[i]))
    checked[fret_candidates[i].index(min(fret_candidates[i]))] = True

for i in range(N):
    if checked[i] == True:
        continue
    else:
        final_fret.append(min(frets[i]))

min_fret = float('inf')
max_fret = 0

for f in final_fret:
    if f != 0:
        if f < min_fret:
            min_fret = f
        elif f > max_fret:
            max_fret = f

print(max_fret, min_fret)
print(max_fret - min_fret + 1)

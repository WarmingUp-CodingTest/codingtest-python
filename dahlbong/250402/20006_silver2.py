import sys
input = sys.stdin.readline

def matching(level, id):
    for i in range(len(game_room)):
        if abs(level - game_room[i][0][0]) <= 10 and len(game_room[i]) < m:
            game_room[i].append([level, id])
            return
    game_room.append([[level, id]])

p, m = map(int, input().split())
players = [[int(l), n] for l, n in (input().split() for _ in range(p))]
game_room = []

for l, n in players:
    matching(l, n)

for room in game_room:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for r in sorted(room, key=lambda x: x[1]):
        print(*r)

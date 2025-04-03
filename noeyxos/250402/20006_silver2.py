from collections import deque


p, m = map(int, input().split())
players = []
for _ in range(p): 
    level, nickname = input().split()
    players.append([int(level), nickname])

rooms = deque([])

def make_game(player_level, player_nickname):
    for room in rooms: 
        if len(room) <m and abs(player_level - room[0][0]) <= 10: 
            room.append([player_level, player_nickname]) 
            return 
    
    rooms.append(deque([[player_level, player_nickname]]))

for player_level, player_nickname in players:
    make_game(player_level, player_nickname)

for room in rooms: 
    if len(room) == m :
        print("Started!")
    else: 
        print("Waiting!")

    for player_level, player_nickname in sorted(room, key=lambda x: x[1]):
        print(player_level, player_nickname)

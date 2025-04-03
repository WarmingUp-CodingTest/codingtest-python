p, m = map(int, input().split())

rooms = []

class room:
  def __init__(self, leader_level, leader_nickname):
    self.leader_level = leader_level
    self.players = []
    self.players.append([leader_level, leader_nickname])
    self.player = 1
  
  def check(self, level):
    if self.player >= m:
      return False
    if self.leader_level - 10 > level or self.leader_level + 10 < level:
      return False
    return True
  
  def enter(self, level, nickname):
    self.player += 1
    self.players.append([level, nickname])
  
  def print_players(self):
    self.players = sorted(self.players, key=lambda player: player[1])
    for i in self.players:
      print(i[0], i[1])
  
  def print_game_start(self):
    if self.player >= m:
      print("Started!")
      return
    print("Waiting!")
  

for i in range(p):
  l, n = input().split()
  l = int(l)
  is_enter = False
  
  for j in rooms:
    if not is_enter and j.check(l):
      j.enter(l, n)
      is_enter = True
  
  if not is_enter:
    new_room = room(l, n)
    rooms.append(new_room)

for i in rooms:
  i.print_game_start()
  i.print_players()
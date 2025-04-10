from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

def team_score(team): 
        score = 0
        for i, j in combinations(team, 2): 
            score += S[i][j] + S[j][i]
        return score

for team in combinations(range(n), n//2): 
    start_team = list(team)
    link_team = [x for x in range(n) if x not in start_team]   

    start_score = team_score(start_team)
    link_score = team_score(link_team)
    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

print(min_diff)
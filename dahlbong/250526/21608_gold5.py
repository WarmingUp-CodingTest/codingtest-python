# 상어 초등학교

import sys, heapq
input = sys.stdin.readline
N = int(input())
students = {}
seats = [[0] * N for _ in range(N)]

def occupy_seats(s, likes):
    candidates = []
    for i in range(N):
        for j in range(N):
            if seats[i][j] != 0:
                continue
            like, empty = 0, 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx,  j + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if seats[nx][ny] in likes:
                        like += 1
                    elif seats[nx][ny] == 0:
                        empty += 1
            heapq.heappush(candidates, (-like, -empty, i, j))
    _, _, x, y = heapq.heappop(candidates)
    seats[x][y] = s

def calc_satisfaction():
    score = 0
    for i in range(N):
        for j in range(N):
            s = seats[i][j]
            likes = students[s]
            cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if seats[nx][ny] in likes:
                        cnt += 1
            if cnt != 0:
                score += 10 ** (cnt - 1)
    return score
    

for _ in range(N**2):
    idx, *likes = map(int, input().split())
    students[idx] = set(likes)

for student, likes in students.items():
    occupy_seats(student, likes)

print(calc_satisfaction())
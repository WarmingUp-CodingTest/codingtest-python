n = int(input())
students = []
likes = {}

for _ in range(n * n):
    line = list(map(int, input().split()))
    student_num = line[0]
    student_likes = line[1:]
    students.append(student_num)
    likes[student_num] = student_likes

classroom = [[0] * n for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_adjacent_positions(r, c):
    adjacent = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            adjacent.append((nr, nc))
    return adjacent

def find_best_position(student_num):
    best_positions = []
    max_liked_count = -1
    max_empty_count = -1
    
    for r in range(n):
        for c in range(n):
            if classroom[r][c] != 0:
                continue
                
            adjacent_positions = get_adjacent_positions(r, c)
            liked_count = 0
            empty_count = 0
            
            for ar, ac in adjacent_positions:
                if classroom[ar][ac] in likes[student_num]:
                    liked_count += 1
                elif classroom[ar][ac] == 0:
                    empty_count += 1
            
            if liked_count > max_liked_count:
                max_liked_count = liked_count
                max_empty_count = empty_count
                best_positions = [(r, c)]
            elif liked_count == max_liked_count:
                if empty_count > max_empty_count:
                    max_empty_count = empty_count
                    best_positions = [(r, c)]
                elif empty_count == max_empty_count:
                    best_positions.append((r, c))
    
    best_positions.sort()
    return best_positions[0]

for student_num in students:
    r, c = find_best_position(student_num)
    classroom[r][c] = student_num

total_satisfaction = 0
satisfaction_scores = [0, 1, 10, 100, 1000]

for r in range(n):
    for c in range(n):
        student_num = classroom[r][c]
        adjacent_positions = get_adjacent_positions(r, c)
        liked_adjacent_count = 0
        
        for ar, ac in adjacent_positions:
            if classroom[ar][ac] in likes[student_num]:
                liked_adjacent_count += 1
        
        total_satisfaction += satisfaction_scores[liked_adjacent_count]

print(total_satisfaction)
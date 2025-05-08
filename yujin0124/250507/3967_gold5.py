lines = [
    [(0, 4), (1, 3), (2, 2), (3, 1)],
    [(0, 4), (1, 5), (2, 6), (3, 7)],
    [(1, 1), (1, 3), (1, 5), (1, 7)],
    [(3, 1), (3, 3), (3, 5), (3, 7)],
    [(1, 1), (2, 2), (3, 3), (4, 4)],
    [(1, 7), (2, 6), (3, 5), (4, 4)]
]

def sol():
    star = [list(input().strip()) for _ in range(5)]
    
    empty = []
    for i in range(5):
        for j in range(9):
            if star[i][j] == 'x':
                empty.append((i, j))
                
    used = [False] * 13
    for i in range(5):
        for j in range(9):
            if 'A' <= star[i][j] <= 'L':
                num = ord(star[i][j]) - ord('A') + 1
                used[num] = True
    
    def get_value(i, j):
        if 'A' <= star[i][j] <= 'L':
            return ord(star[i][j]) - ord('A') + 1
        return 0
    
    def back(idx):
        if idx == len(empty):
            for line in lines:
                total = sum(get_value(i, j) for i, j in line)
                if total != 26:
                    return False
            return True
        
        x, y = empty[idx]
        
        for num in range(1, 13):
            if not used[num]:
                star[x][y] = chr(ord('A') + num - 1)
                used[num] = True
                
                valid = True
                for line in lines:
                    if (x, y) in line:
                        filled = True
                        for lx, ly in line:
                            if star[lx][ly] == 'x':
                                filled = False
                                break
                        
                        if filled:
                            total = sum(get_value(i, j) for i, j in line)
                            if total != 26:
                                valid = False
                                break
                
                if valid and back(idx + 1):
                    return True
                
                star[x][y] = 'x'
                used[num] = False
        
        return False
    
    back(0)
    
    for row in star:
        print(''.join(row))

sol()
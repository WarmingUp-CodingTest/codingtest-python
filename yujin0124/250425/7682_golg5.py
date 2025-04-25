def check_win(mark):
    for i in range(3):
        if arr[i][0] == mark and arr[i][1] == mark and arr[i][2] == mark:
            return True
        
    for i in range(3):
        if arr[0][i] == mark and arr[1][i] == mark and arr[2][i] == mark:
            return True
        
    if arr[0][0] == mark and arr[1][1] == mark and arr[2][2] == mark:
        return True
    if arr[0][2] == mark and arr[1][1] == mark and arr[2][0] == mark:
        return True
    
    return False

while True:
    str = input().strip()
    if str == "end":
        break
    
    arr = [['a'] * 3 for _ in range(3)]
    count_x = 0
    count_o = 0
    count_dot = 0
    index = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = str[index]
            if arr[i][j] == 'X':
                count_x += 1
            elif arr[i][j] == 'O':
                count_o += 1
            else:
                count_dot += 1
            index += 1
    
    if count_x > count_o + 1 or count_o > count_x:
        print("invalid")
        continue
    
    x_win = check_win('X')
    o_win = check_win('O')
    
    if x_win and o_win:
        print('invalid')
        continue
    
    if x_win and count_x != count_o + 1:
        print('invalid')
        continue
    
    if o_win and count_x != count_o:
        print('invalid')
        continue
    
    is_game_over = (count_dot == 0) or x_win or o_win
    
    if not is_game_over:
        print('invalid')
        continue
    
    print('valid')
def solution(board):
    lines = []
    for i in range(3):
        lines.append(board[i])
        lines.append(''.join(row[i] for row in board))
        
    lines.append(''.join(board[i][i] for i in range(3)))
    lines.append(''.join(board[2 - i][i] for i in range(3)))

    o_win = 'OOO' in lines
    x_win = 'XXX' in lines

    o = sum(row.count('O') for row in board)
    x = sum(row.count('X') for row in board)

    if x > o or o > x + 1:
        return 0
    
    if o_win and x_win:
        return 0
    
    if o_win and o != x + 1:
        return 0
    
    if x_win and o != x:
        return 0
    
    return 1

def solution(board, moves):
    answer = 0
    n, m = len(board), len(board[0])
    stack = []
    for x in moves:
        x -= 1
        for y in range(m):
            if board[y][x]:
                if stack and stack[-1] == board[y][x]:
                    stack.pop()
                    board[y][x] = 0
                    answer += 2
                    
                else:
                    stack.append(board[y][x])
                    board[y][x] = 0
                
                break
                
    return answer

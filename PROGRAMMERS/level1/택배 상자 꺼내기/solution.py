def solution(n, w, num):
    answer = 0
    pos = {}
    dx = 1
    y, x = 0, 0
    sy, sx = 0, 0
    idx = 1
    while idx <= n:
        pos[(y, x)] = idx
        if idx == num:
            sy, sx = y, x
            
        x += dx
        idx += 1
        if x == w:
            x, dx = w - 1, -1
            y += 1
            
        elif x < 0:
            x, dx = 0, 1
            y += 1
            
    while pos.get((sy, sx)) != None:
        answer += 1
        sy += 1

    return answer
def solution(n, m, x, y, r, c, k):
    answer = ''
    direction = {'d': (1, 0), 'u': (-1, 0), 'l': (0, -1), 'r': (0, 1)}
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2:
        return 'impossible'
    
    for _ in range(k):
        for d in 'dlru':
            dx, dy = direction[d]
            xx, yy = x + dx, y + dy
            if xx < 1 or xx > n or yy < 1 or yy > m:
                continue
                
            dist = abs(xx - r) + abs(yy - c)
            remain = k - len(answer) - 1
            if dist <= remain and not (remain - dist) % 2:
                answer += d
                x, y = xx, yy
                break
    
    return answer

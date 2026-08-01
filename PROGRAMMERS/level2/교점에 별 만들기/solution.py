def solution(line):
    answer = []
    
    def get_pos(i, j):
        a, b, e = line[i]
        c, d, f = line[j]
        k = (a * d) - (b * c)
        if not k:
            return 0
        
        vx = b * f - e * d
        vy = c * e - a * f
        if vx % k or vy % k:
            return 0
        
        x = vx // k
        y = vy // k
        return [x, y]
    
    pos = []
    l = len(line)
    for i in range(l):
        for j in range(i + 1, l):
            p = get_pos(i, j)
            if not p:
                continue
            
            pos.append(p)

    xs = [p[0] for p in pos]
    ys = [p[1] for p in pos]
    mx, mmx = min(xs), max(xs)
    my, mmy = min(ys), max(ys)
            
    for p in pos:
        p[0] -= mx
        p[1] -= my
        
    mmx -= mx
    mmy -= my

    arr = [['.'] * (mmx + 1) for _ in range(mmy + 1)]
    for x, y in pos:
        arr[mmy - y][x] = '*'            
    
    for l in arr:
        answer.append(''.join(l))
        
    return answer

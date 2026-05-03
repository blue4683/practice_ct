def solution(wallpaper):
    n, m = len(wallpaper), len(wallpaper[0])
    lty, ltx = n, m
    rty, rtx = 0, 0
    for y in range(n):
        for x in range(m):
            if wallpaper[y][x] == '#':
                if y < lty:
                    lty = y

                if x < ltx:
                    ltx = x

                if y + 1 > rty:
                    rty = y + 1

                if x + 1 > rtx:
                    rtx = x + 1

    answer = [lty, ltx, rty, rtx]
    return answer

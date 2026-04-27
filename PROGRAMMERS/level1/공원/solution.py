def solution(mats, park):
    answer = 0
    n, m = len(park), len(park[0])
    mats.sort(reverse=True)

    def check(sy, sx, k):
        for y in range(sy, sy + k):
            for x in range(sx, sx + k):
                if y < 0 or y >= n or x < 0 or x >= m or park[y][x] != '-1':
                    return 0

        return 1

    for y in range(n):
        for x in range(m):
            if park[y][x] != '-1':
                continue

            for mat in mats:
                if answer >= mat:
                    break

                if check(y, x, mat):
                    answer = mat
                    break

    return answer if answer else -1

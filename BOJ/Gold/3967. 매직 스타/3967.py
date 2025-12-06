import sys
input = sys.stdin.readline


def print_stars(stars):
    for i in range(12):
        y, x = index[i]
        arr[y][x] = chr(stars[i] + ord('A') - 1)

    for line in arr:
        print(''.join(line))


def check():
    lines = [[0, 2, 5, 7], [0, 3, 6, 10], [1, 2, 3, 4],
             [1, 5, 8, 11], [4, 6, 9, 11], [7, 8, 9, 10]]
    for line in lines:
        tmp = 0
        for j in line:
            tmp += stars[j]

        if tmp != 26:
            return 0

    return 1


def fill(i, possible):
    if i == 12:
        if check():
            print_stars(stars)
            exit()

        return

    if stars[i]:
        fill(i + 1, possible)

    else:
        for j in range(1, 13):
            if j not in possible:
                continue

            stars[i] = j
            fill(i + 1, possible - {j})
            stars[i] = 0


def init():
    index = {}
    idx = 0

    stars = [arr[0][4]]
    index[idx] = (0, 4)
    idx += 1

    for i in range(1, 9, 2):
        stars.append(arr[1][i])
        index[idx] = (1, i)
        idx += 1

    stars.append(arr[2][2])
    index[idx] = (2, 2)
    idx += 1
    stars.append(arr[2][-3])
    index[idx] = (2, -3)
    idx += 1

    for i in range(1, 9, 2):
        stars.append(arr[3][i])
        index[idx] = (3, i)
        idx += 1

    stars.append(arr[4][4])
    index[idx] = (4, 4)

    for i in range(12):
        stars[i] = 0 if stars[i] == 'x' else ord(stars[i]) - ord('A') + 1

    possible = {i for i in range(1, 13)}
    for i in range(12):
        if stars[i]:
            possible.remove(stars[i])

    return stars, index, possible


arr = [list(input().rstrip()) for _ in range(5)]
stars, index, possible = init()
fill(0, possible)

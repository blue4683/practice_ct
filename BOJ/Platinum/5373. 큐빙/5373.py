import sys
input = sys.stdin.readline
side = {s: i for i, s in enumerate('UDFBLR')}


def rotate(s):
    tmp = [[''] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tmp[j][2 - i] = cube[side[s]][i][j]

    cube[side[s]] = tmp


def turn(s, rotation):
    if rotation == '-':
        for _ in range(3):
            turn(s, '+')

        return

    rotate(s)
    if s == 'U':
        cube[2][0], cube[5][0], cube[3][0], cube[4][0] = cube[5][0], cube[3][0], cube[4][0], cube[2][0]

    elif s == 'D':
        cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[4][2], cube[3][2], cube[5][2], cube[2][2]

    elif s == 'F':
        temp = cube[0][2]
        cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = [
            cube[1][0][0], cube[1][0][1], cube[1][0][2]]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = [
            cube[5][2][0], cube[5][1][0], cube[5][0][0]]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = [
            temp[0], temp[1], temp[2]]

    elif s == 'B':
        temp = cube[0][0]
        cube[0][0] = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = [
            cube[1][2][2], cube[1][2][1], cube[1][2][0]]
        cube[1][2][2], cube[1][2][1], cube[1][2][0] = [
            cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        cube[4][2][0], cube[4][1][0], cube[4][0][0] = [
            temp[0], temp[1], temp[2]]

    elif s == 'L':
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        cube[0][2][0], cube[0][1][0], cube[0][0][0] = [
            cube[3][0][2], cube[3][1][2], cube[3][2][2]]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = [
            cube[1][2][0], cube[1][1][0], cube[1][0][0]]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = [
            cube[2][0][0], cube[2][1][0], cube[2][2][0]]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = [
            temp[0], temp[1], temp[2]]

    else:
        temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = [
            cube[2][0][2], cube[2][1][2], cube[2][2][2]]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = [
            cube[1][0][2], cube[1][1][2], cube[1][2][2]]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = [
            cube[3][2][0], cube[3][1][0], cube[3][0][0]]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = [
            temp[0], temp[1], temp[2]]


for _ in range(int(input())):
    n = int(input())
    cube = [[[color] * 3 for _ in range(3)] for color in 'wyrogb']
    for commands in input().split():
        s, rotation = list(commands)
        turn(s, rotation)

    for l in cube[0]:
        print(''.join(l))

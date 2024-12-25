import math
import sys
input = sys.stdin.readline


def use_size_1(remain):
    if paper[1] <= remain:
        remain -= paper[1]
        paper[1] = 0

    else:
        paper[1] -= remain
        remain = 0

    return remain


paper = [0] + [int(input()) for _ in range(6)]
result = paper[6]
remain = 0
if paper[5]:
    result += paper[5]
    remain += paper[5] * 11
    remain = use_size_1(remain)

if paper[4]:
    result += paper[4]
    if paper[2]:
        if paper[2] <= paper[4] * 5:
            remain += paper[4] * 20 - paper[2] * 4
            paper[2] = 0

        else:
            paper[2] -= paper[4] * 5

    remain = use_size_1(remain)

if paper[3]:
    result += math.ceil(paper[3] / 4)
    mod = paper[3] % 4
    if mod:
        if paper[2] <= 2 * (4 - mod) - 1:
            remain += 36 - (mod * 9) - (paper[2] * 4)
            paper[2] = 0

        else:
            paper[2] -= 2 * (4 - mod) - 1
            remain += 36 - (mod * 9) - ((2 * (4 - mod) - 1) * 4)

    remain = use_size_1(remain)

if paper[2]:
    result += math.ceil(paper[2] / 9)
    mod = paper[2] % 9
    if mod:
        remain += 36 - (4 * mod)

    remain = use_size_1(remain)

if paper[1]:
    result += math.ceil(paper[1] / 36)

print(result)

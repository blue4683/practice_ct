from collections import deque
import sys
input = sys.stdin.readline


def rotate(index, direction):
    is_rotated = [0] * 4
    is_rotated[index] = direction

    for i in range(index - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            is_rotated[i] = -is_rotated[i + 1]

    for i in range(index + 1, 4):
        if gears[i][6] != gears[i - 1][2]:
            is_rotated[i] = -is_rotated[i - 1]

    for i in range(4):
        gear = gears[i]
        if is_rotated[i] == 1:
            gear.appendleft(gear.pop())

        elif is_rotated[i] == -1:
            gear.append(gear.popleft())


gears = [deque(map(int, list(input().rstrip()))) for _ in range(4)]
k = int(input())
rotations = [list(map(int, input().split())) for _ in range(k)]

for index, direction in rotations:
    rotate(index - 1, direction)

result = 0
for i in range(4):
    if gears[i][0]:
        result |= 1 << i

print(result)

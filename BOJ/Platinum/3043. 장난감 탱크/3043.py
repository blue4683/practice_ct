import sys
input = sys.stdin.readline


def up_down(arr):
    up, down = [], []
    for i in range(1, n + 1):
        y, _, _ = arr[i - 1]
        if y > i:
            up.append(i)

        if y < i:
            down.append(i)

    for i in up:
        for _ in range(arr[i - 1][0] - i):
            result.append((arr[i - 1][-1], 'U'))

    down.sort(reverse=True)
    for i in down:
        for _ in range(i - arr[i - 1][0]):
            result.append((arr[i - 1][-1], 'D'))


def left_right(arr):
    left, right = [], []
    for i in range(1, n + 1):
        _, x, _ = arr[i - 1]
        if x > i:
            left.append(i)

        if x < i:
            right.append(i)

    for i in left:
        for _ in range(arr[i - 1][1] - i):
            result.append((arr[i - 1][-1], 'L'))

    right.sort(reverse=True)
    for i in right:
        for _ in range(i - arr[i - 1][1]):
            result.append((arr[i - 1][-1], 'R'))


n = int(input())
tanks = [(*map(int, input().split()), i) for i in range(1, n + 1)]
result = []
up_down(sorted(tanks))
left_right(sorted(tanks, key=lambda x: x[1]))

print(len(result))
for num, dir in result:
    print(num, dir)

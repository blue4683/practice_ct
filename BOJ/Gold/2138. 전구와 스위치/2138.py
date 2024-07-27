import sys
input = sys.stdin.readline


def push(index):
    for i in range(index - 1, index + 2):
        if i < 0 or i >= n:
            continue

        arr[i] = 1 - arr[i]

    return


n = int(input())
light = list(map(int, list(input().rstrip())))
target = list(map(int, list(input().rstrip())))

result = 10 ** 9
for i in range(2):
    cnt = i
    arr = light[:]

    if i:
        push(0)

    for j in range(1, n):
        if arr[j - 1] != target[j - 1]:
            push(j)
            cnt += 1

    if arr == target:
        result = min(result, cnt)

print(result) if result != 10 ** 9 else print(-1)

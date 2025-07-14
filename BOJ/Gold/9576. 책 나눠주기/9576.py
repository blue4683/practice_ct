import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    students = sorted([tuple(map(int, input().split())) for _ in range(m)])
    arr = [[0] * (n + 1) for _ in range(m)]

    for i in range(m):
        for j in range(students[i][0], students[i][1] + 1):
            arr[i][j] = 1

    result = 0
    for i in range(1, n + 1):
        tmp = []
        for j in range(m):
            if arr[j][i]:
                tmp.append(j)

        if not tmp:
            continue

        v, idx = 1001, 0
        for j in tmp:
            if v <= sum(arr[j]):
                continue

            v = sum(arr[j])
            idx = j

        for j in range(m):
            arr[j][i] = 0

        for j in range(1, n + 1):
            arr[idx][j] = 0

        result += 1

    print(result)

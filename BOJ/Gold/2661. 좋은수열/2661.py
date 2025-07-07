import sys
input = sys.stdin.readline


def check(num):
    for k in range(1, len(num)):
        if k * 2 > len(num):
            break

        s, e = 0, k
        while e < len(num):
            a, b = num[s:e], num[e:e + k]
            if a == b:
                return 0

            s += 1
            e += 1

    return 1


def dfs(num):
    global result
    if result:
        return

    if len(num) == n:
        result = num
        return

    for i in range(1, 4):
        if check(num + str(i)):
            dfs(num + str(i))


n = int(input())
result = 0
dfs('')
print(result)

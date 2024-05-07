import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def check(start, end):
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1

        else:
            if check_similar(start + 1, end) or check_similar(start, end - 1):
                return 1

            return 2

    return 0


def check_similar(start, end):
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1

        else:
            return 0

    return 1


for _ in range(int(input())):
    string = input().rstrip()
    start, end = 0, len(string) - 1
    result = check(start, end)

    print(result)

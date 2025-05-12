import sys
input = sys.stdin.readline


def get_result(minus):
    k = len(str(n)) + 1
    search_range = range(n, -1, -1) if minus else range(n, 10 ** k)
    for i in search_range:
        channel = str(i)
        for num in channel:
            if int(num) in broken:
                break

        else:
            return abs(n - i) + len(channel)

    return 0


n = int(input())
m = int(input())
broken = set(map(int, input().split())) if m else set()

result = abs(n - 100)
for minus in [0, 1]:
    cnt = get_result(minus)
    if cnt:
        result = min(result, cnt)

print(result)

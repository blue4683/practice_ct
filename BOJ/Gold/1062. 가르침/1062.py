from itertools import combinations
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
words = [set(input().rstrip()[4:-4]) for _ in range(n)]
if k < 5:
    print(0)

elif k == 26:
    print(n)

else:
    essential = set('acint')
    able = set()
    for word in words:
        able |= word

    able -= essential
    if len(able) <= k - 5:
        print(n)

    else:
        cases = combinations(able, k - 5)
        result = 0
        for cs in cases:
            known = set(cs) | essential
            cnt = 0
            for word in words:
                if word.issubset(known):
                    cnt += 1

            result = max(result, cnt)

        print(result)

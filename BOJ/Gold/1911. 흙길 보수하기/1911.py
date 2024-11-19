import math
import sys
input = sys.stdin.readline


n, l = map(int, input().split())
puddles = [tuple(map(int, input().split())) for _ in range(n)]
puddles.sort()

result = 0
end = puddles[0][0]
for a, b in puddles:
    if a > end:
        end = a

    dist = b - end
    result += math.ceil(dist / l)
    if not dist % l:
        end = b

    else:
        end = b + (l - dist % l)

print(result)

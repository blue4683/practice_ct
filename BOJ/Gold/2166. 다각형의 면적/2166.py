import sys

input = sys.stdin.readline


class P:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def get_area(A, B):
    S = (A.x + B.x) * (A.y - B.y)
    return S


n = int(input())
pos = [P(*map(int, input().split())) for _ in range(n)]
pos.append(pos[0])
result = 0

for i in range(n):
    result += get_area(pos[i], pos[i + 1])

print(round(abs(result) / 2, 1))

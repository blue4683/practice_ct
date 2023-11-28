import sys

input = sys.stdin.readline


class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y


A, B, C = (
    P(*map(int, input().split())),
    P(*map(int, input().split())),
    P(*map(int, input().split())),
)

result = (A.x * B.y + B.x * C.y + C.x * A.y) - (A.y * B.x + B.y * C.x + C.y * A.x)

print(0) if not result else print(result // abs(result))

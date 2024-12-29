import math
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    blocks = [list(input().rstrip()) for _ in range(2)]
    print(math.ceil(sum(map(int, blocks[0])) / 3))

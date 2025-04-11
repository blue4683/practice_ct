import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, m = map(int, input().split())
    planes = [list(map(int, input().split())) for _ in range(m)]
    print(n - 1)

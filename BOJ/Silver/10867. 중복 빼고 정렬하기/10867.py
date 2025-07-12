import sys
input = sys.stdin.readline

n = int(input())
print(*sorted(set(map(int, input().split()))))

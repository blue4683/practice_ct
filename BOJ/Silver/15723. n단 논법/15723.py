import sys
input = sys.stdin.readline


def convert(alp):
    return ord(alp) - ord('a')


n = int(input())
graph = [[0] * 26 for _ in range(26)]
for _ in range(n):
    u, _, v = input().split()
    graph[convert(u)][convert(v)] = 1

for mid in range(26):
    for s in range(26):
        for e in range(26):
            if graph[s][mid] and graph[mid][e]:
                graph[s][e] = 1

for _ in range(int(input())):
    u, _, v = input().split()
    print('T') if graph[convert(u)][convert(v)] else print('F')

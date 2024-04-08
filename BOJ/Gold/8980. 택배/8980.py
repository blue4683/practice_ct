from collections import deque
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
boxes = [list(map(int, input().split())) for _ in range(m)]

boxes.sort(key=lambda x: x[1])
boxes = deque(boxes)

result = 0
capacity = [c] * n

for now, next, box in boxes:
    capa = c
    for i in range(now, next):
        if capa > min(capacity[i], box):
            capa = min(capacity[i], box)

    for i in range(now, next):
        capacity[i] -= capa

    result += capa

print(result)

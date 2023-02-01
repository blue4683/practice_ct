import sys
input = sys.stdin.readline

n = int(input())
tasks = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])
tasks = sorted(tasks, key=lambda x:x[-1])
start, end = tasks[0]
cnt = 1
for task in tasks[1:]:
    if task[0] >= end:
        cnt += 1
        start, end = task
print(cnt)
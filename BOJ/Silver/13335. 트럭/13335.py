from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
q = deque([0] * w)

time = 0
while trucks:
    time += 1
    q.popleft()

    if sum(q) + trucks[0] <= l:
        q.append(trucks.popleft())

    else:
        q.append(0)

while q:
    time += 1
    q.popleft()

print(time)

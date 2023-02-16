from queue import PriorityQueue
import sys
input = sys.stdin.readline

n=int(input())
q=PriorityQueue()
for x in [int(input()) for _ in range(n)]:
    if not x:
        if q.empty():
            print(0)
        else:
            print(q.get()[1])
    else:
        q.put((abs(x),x))
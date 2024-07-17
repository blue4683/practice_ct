from collections import deque
import sys
input = sys.stdin.readline


def step1():
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    robot[n - 1] = 0


def step2():
    for i in range(n - 2, -1, -1):
        if not robot[i] or robot[i + 1] or not belt[i + 1]:
            continue

        robot[i], robot[i + 1] = robot[i + 1], robot[i]
        belt[i + 1] -= 1

    robot[n - 1] = 0


def step3():
    if not belt[0]:
        return

    robot[0] = 1
    belt[0] -= 1


def step4():
    global result
    if belt.count(0) >= k:
        return 1

    result += 1
    return 0


n, k = map(int, input().split())
arr = list(map(int, input().split()))
belt = deque(arr)
robot = deque([0] * (2 * n))
result = 0

while not step4():
    step1()
    step2()
    step3()

print(result)

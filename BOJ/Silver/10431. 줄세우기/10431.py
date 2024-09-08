import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    t = arr[0]
    stack = []
    result = 0
    for next_height in arr[1:]:
        for height in stack:
            if height > next_height:
                result += 1

        stack.append(next_height)

    print(t, result)

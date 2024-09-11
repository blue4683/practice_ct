import sys
input = sys.stdin.readline

n, m = map(int, input().split())
back = []
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        back.append((b, a))

if not back:
    print(m)

else:
    back.sort()
    arrival = back[0][1]
    distance = back[0][1] - back[0][0]

    for start, end in back[1:]:
        if arrival >= start:
            if arrival < end:
                distance += end - arrival
                arrival = end

        else:
            distance += end - start
            arrival = end

    print(distance * 2 + m)

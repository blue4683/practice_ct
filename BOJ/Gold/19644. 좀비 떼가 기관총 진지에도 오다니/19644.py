import sys
input = sys.stdin.readline

l = int(input())
ml, mk = map(int, input().split())
ammo = int(input())
zombies = [int(input()) for _ in range(l)]
result = 1

arr = [0] * l
for i in range(l):
    now = arr[i - 1] if i <= ml else arr[i - 1] - arr[i - ml]
    if zombies[i] <= now + mk:
        arr[i] = arr[i - 1] + mk
        continue

    else:
        if not ammo:
            result = 0
            break

        ammo -= 1
        arr[i] = arr[i - 1]

print('YES' if result else 'NO')

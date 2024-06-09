import sys
input = sys.stdin.readline

n = int(input())
result = 0

for _ in range(n):
    word = input().rstrip()
    used = set()
    before = ''
    for char in word:
        if before == char:
            continue

        before = char
        if char in used:
            break

        else:
            used.add(char)

    else:
        result += 1

print(result)

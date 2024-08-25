import sys
input = sys.stdin.readline

n, k = map(int, input().split())
string = input().rstrip()

result = [0] * n
for i in range(n):
    if string[i] == 'P':
        for j in range(-k, k + 1):
            if i + j < 0 or i + j >= n:
                continue

            if string[i + j] == 'H' and not result[i + j]:
                result[i] = 1
                result[i + j] = 1
                break

print(sum(result) // 2)

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
counter = defaultdict(int)
not_zero = defaultdict(int)
for word in words:
    m = len(word)
    not_zero[word[0]] = 1
    for i in range(m):
        counter[word[m - 1 - i]] += 10 ** i

alps = sorted(counter.items(), key=lambda x: x[-1])
k = len(alps)
alp_num = defaultdict(str)

for alp, _ in alps:
    for i in range(10 - k, 10):
        if str(i) in alp_num.values():
            continue

        if not i and not_zero[alp]:
            continue

        alp_num[alp] = str(i)
        break

numbers = []
for word in words:
    numbers.append(int(''.join(map(lambda x: alp_num[x], list(word)))))

print(sum(numbers))

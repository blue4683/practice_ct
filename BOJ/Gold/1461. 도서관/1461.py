import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

positive, negative = [], []
for book in books:
    if book > 0:
        positive.append(book)

    else:
        negative.append(-book)

positive.sort(reverse=True)
negative.sort(reverse=True)

result = 0
for i in range(0, len(positive), m):
    result += positive[i] * 2

for i in range(0, len(negative), m):
    result += negative[i] * 2

if positive and negative:
    if positive[0] > negative[0]:
        result -= positive[0]

    else:
        result -= negative[0]

elif positive:
    result -= positive[0]

else:
    result -= negative[0]

print(result)

n = int(input())
scores = list(map(int,input().split()))
max_score = 0

for score in scores:
    max_score = score if score>max_score else max_score
new_scores = list(map(lambda x:x*100/max_score, scores))

sum_scores = 0
for score in new_scores:
    sum_scores += score

result = sum_scores/n
print(result)
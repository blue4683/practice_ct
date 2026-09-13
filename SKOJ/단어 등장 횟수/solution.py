n, q = map(int, input().split())
words = {}
for _ in range(n):
    word = input().rstrip()
    if word not in words:
        words[word] = 0
        
    words[word] += 1

result = []
for _ in range(q):
    word = input().rstrip()
    if word not in words:
        words[word] = 0
    
    print(words[word])
    
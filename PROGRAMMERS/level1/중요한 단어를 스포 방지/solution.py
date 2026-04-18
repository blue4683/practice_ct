def is_in_range(s, e, sr, se):
    return s <= sr <= e or s <= se <= e or sr <= s <= se or sr <= e <= se


def solution(message, spoiler_ranges):
    answer = 0
    words = message.split()
    ranges = [(0, len(words[0]) - 1) if message[0] != ' ' else (1, len(words[0]))]
    for i in range(1, len(words)):
        s = ranges[i - 1][1] + 2
        ranges.append((s, s + len(words[i]) - 1))

    spoilers = []
    for sr, se in spoiler_ranges:
        tmp = []
        for i in range(len(ranges)):
            s, e = ranges[i]
            if is_in_range(s, e, sr, se):
                tmp.append(i)
                
        spoilers.append(tmp)
    
    remain, spoiler, used = set(), [], set()
    for r in spoilers:
        tmp = []
        for i in r:
            tmp.append(words[i])
            used.add(i)
        
        spoiler.append(tmp)
        
    for i in range(len(words)):
        if i not in used:
            remain.add(words[i])

    for w in spoiler:
        for word in w:
            if word not in remain:
                answer += 1
                
            remain.add(word)
    
    return answer
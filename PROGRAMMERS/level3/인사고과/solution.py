def solution(scores):
    answer = 1
    arr = [-1] * 100002
    n = len(scores)
    max_score = -1
    for i in range(n):
        a, b = scores[i]
        idx = arr[a]
        max_score = max(max_score, a)
        if idx == -1 or scores[idx][1] < b:
            arr[a] = i
    
    idx = arr[max_score]
    for i in range(max_score - 1, -1, -1):
        new_idx = arr[i]
        if new_idx == -1 or scores[idx][1] >= scores[new_idx][1]:
            arr[i] = idx
            
        else:
            idx = new_idx
            arr[i] = idx

    a, b = scores[0]
    idx = arr[a + 1]
    if idx >= 0 and scores[idx][1] > b:
        return -1
    
    for i in range(1, n):
        a, b = scores[i]
        idx = arr[a + 1]
        if (idx >= 0 and scores[idx][1] > b) or (sum(scores[0]) >= a + b):
            continue
            
        answer += 1

    return answer

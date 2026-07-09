def solution(sequence):
    n = len(sequence)
    v1, v2 = sequence[0], -sequence[0]
    answer = max(v1, v2)
    for i in range(1, n):
        if i % 2:
            v1 = max(-sequence[i], v1 - sequence[i])
            v2 = max(sequence[i], v2 + sequence[i])
            
        else:
            v1 = max(sequence[i], v1 + sequence[i])
            v2 = max(-sequence[i], v2 - sequence[i])
            
        answer = max(answer, v1, v2)

    return answer

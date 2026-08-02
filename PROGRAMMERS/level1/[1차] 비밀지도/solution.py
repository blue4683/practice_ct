from math import log2


def solution(n, arr1, arr2):
    answer = []
    a, b = max(arr1), max(arr2)
    m = max(a, b)
    m = int(log2(m)) + 1
    
    for l1, l2 in zip(arr1, arr2):
        v = bin(l1 | l2)[2:].zfill(m)
        answer.append(''.join(map(lambda x: '#' if x == '1' else ' ', v)))
        
    return answer

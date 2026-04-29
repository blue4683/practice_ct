def solution(name, yearning, photo):
    answer = []
    n = len(name)
    index = {name[i]: i for i in range(n)}
    for arr in photo:
        answer.append(sum(map(lambda x: yearning[index[x]] if x in index else 0, arr)))
    
    return answer

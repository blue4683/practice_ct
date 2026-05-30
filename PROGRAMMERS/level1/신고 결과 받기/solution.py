from collections import defaultdict


def solution(id_list, report, k):
    n = len(id_list)
    idx = {id_list[i]: i for i in range(n)}
    answer = [0] * n
    relation = defaultdict(set)
    for r in report:
        a, b = r.split()
        relation[b].add(a)

    for key in relation:
        if len(relation[key]) >= k:
            for id in relation[key]:
                answer[idx[id]] += 1

    return answer

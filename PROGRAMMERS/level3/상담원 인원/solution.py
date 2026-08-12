from heapq import heappop, heappush


def solution(k, n, reqs):
    answer = 0
    times = [0] * (k + 1)
    remain = n - k + 1
    first = [[] for _ in range(k + 1)]
    for cnt in range(remain):
        mentors = [f[:] for f in first]
        ttimes = [0] * (k + 1)
        for i in range(1, k + 1):
            mentors[i].append(0)
            
        for s, e, i in reqs:
            time = heappop(mentors[i])
            if time > s:
                ttimes[i] += (time - s)
                heappush(mentors[i], time + e)

            else:
                heappush(mentors[i], s + e)

        j, diff = 0, -1
        for i in range(1, k + 1):
            if times[i] - ttimes[i] > diff:
                diff = times[i] - ttimes[i]
                j = i
        
        if not cnt:
            times = ttimes[:]
            first = [[0] for _ in range(k + 1)]
            continue
        
        first[j].append(0)
        times[j] = ttimes[j]
            
    return sum(times)

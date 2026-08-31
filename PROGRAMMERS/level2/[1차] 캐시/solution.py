def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.append(cache.pop(cache.index(city)))
        
        else:
            answer += 5
            if cacheSize and len(cache) == cacheSize:
                cache.pop(0)
            
            if cacheSize:
                cache.append(city)
            
    return answer

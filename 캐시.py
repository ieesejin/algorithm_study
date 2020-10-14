# https://programmers.co.kr/learn/courses/30/lessons/17680


def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0: # 캐시가 0 일때
        return len(cities) * 5

    for city in cities:
        city = city.lower() # 대소문자 구분 안함
        if city in cache: # city 가 캐시에 있을 때
            cache.remove(city) # LRU 최근에 사용한걸 계속 맨뒤로 업데이트
            cache.append(city)
            answer += 1
        else: # city 가 캐시에 없을 때
            if len(cache) == cacheSize: # city 가 캐시에 없는데 캐시가 꽉 찾을 때
                cache.pop(0)
                cache.append(city)
                answer += 5
            elif len(cache) < cacheSize: # city 가 캐시에 없는데 캐시 자리가 있을 때
                cache.append(city)
                answer += 5

    return answer

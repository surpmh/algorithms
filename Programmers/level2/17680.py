# [1차] 캐시
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()

    for city in cities:
        city = city.upper()
        
        if city in q:
            answer += 1
        else:
            answer += 5

        if len(q) < cacheSize:
            q.append(city)
        else:
            if city in q:
                q.append(city)
                q.remove(city)
            else:
                q.append(city)
                q.popleft()
        
    return answer

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
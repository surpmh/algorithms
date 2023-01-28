# 구명보트
from collections import deque

def solution(people, limit):
    answer = 0

    people.sort()
    people = deque(people)

    while people:
        sum = people.pop()
        answer += 1

        while people and sum + people[0] <= limit:
            sum += people.popleft()
            
    return answer

print(solution([70, 50, 80, 50], 100))
# 광물 캐기
import math

def dig(part_minerals, pick):
    fatigue = 0

    for mineral in part_minerals:
        fatigue += math.ceil(int(mineral) / pick)

    return fatigue

def solution(picks, minerals):
    minerals = [s.replace("diamond", "25").replace("iron", "5").replace("stone", "1") for s in minerals]
    answer = 0
    part = []

    for i in range(0, sum(picks)*5, 5):
        part.append(minerals[i:i+5])

    part.sort(key=lambda x: sum(int(i) for i in x), reverse=True)

    for p in part:
        if picks[0]:
            answer += dig(p, 25)
            picks[0] -= 1
        elif picks[1]:
            answer += dig(p, 5)
            picks[1] -= 1
        elif picks[2]:
            answer += dig(p, 1)
            picks[2] -= 1

    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
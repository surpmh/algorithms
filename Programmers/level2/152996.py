# 시소 짝꿍
from collections import defaultdict

def solution(weights):
    answer = 0
    dict = defaultdict(int)

    for weight in weights:
        dict[weight] += 1

    for key, value in dict.items():
        if value > 1:
            answer += value * (value - 1) // 2
        if key * 2 in dict:
            answer += value * dict[key * 2]
        if key * 3 % 2 == 0 and key * 3 // 2 in dict :
            answer += value * dict[key * 3 // 2]
        if key * 4 % 3 == 0 and key * 4 // 3 in dict:
            answer += value * dict[key * 4 // 3]

    return answer

print(solution([100,180,360,100,270]))
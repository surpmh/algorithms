# 두 원 사이의 정수 쌍
import math

def solution(r1, r2):
    answer = 0

    for i in range(1, r2+1):
        maxNum = math.floor(math.sqrt(math.pow(r2, 2) - math.pow(i, 2)))
        
        if i < r1:
            minNum = math.ceil(math.sqrt(math.pow(r1, 2) - math.pow(i, 2)))
        else:
            minNum = 0
        
        answer += maxNum - minNum + 1

    return answer * 4

print(solution(2, 3))
# 정수 제곱근 판별
import math

def solution(n):
    return math.pow(math.sqrt(n) + 1, 2) if math.sqrt(n).is_integer() else -1

print(solution(121))
# 소수 찾기
import math

def solution(n):
    answer = 0

    primes = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i] == True:
            for j in range(i + i, n + 1, i):
                primes[j] = False

    for i in range(2, n+1):
        if primes[i]:
            answer += 1

    return answer

print(solution(10))
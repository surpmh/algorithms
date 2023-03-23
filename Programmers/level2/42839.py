# 소수 찾기
from itertools import permutations

def solution(numbers):
    prime = [True] * 100000001
    prime[0], prime[1] = False, False

    for i in range(2, int(10000001 ** 0.5) + 1):
        if prime[i] == True:
            for j in range(i+i, 10000001, i):
                prime[j] = False

    answer = set()

    for i in range(1, len(numbers)+1):
        for j in list(map(''.join, permutations(numbers, i))):
            if prime[int(j)]:
                answer.add(int(j))

    return len(answer)

print(solution("17"))
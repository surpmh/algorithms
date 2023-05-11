# k진수에서 소수 개수 구하기
import math

def solution(n, k):
    answer = 0
    trans = ""

    while n:
        trans = str(n % k) + trans
        n = n // k

    numbers = list(map(str, trans.split("0")))

    for num in numbers:
        prime = True
        if num.isdigit():
            num = int(num)
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime == True and num != 1:
                answer += 1

    return answer

print(solution(437674, 3))
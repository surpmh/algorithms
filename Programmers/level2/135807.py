# 숫자 카드 나누기
import functools

def gcd(iters):
    def _gcd(n, m):
        while m > 0:
            n, m = m, n % m
        return n
    return functools.reduce(_gcd, iters)

def solution(arrayA, arrayB):
    a, b = 0, 0
    numA = gcd(arrayA)
    numB = gcd(arrayB)

    for i in range(len(arrayA)):
        if arrayB[i] % numA == 0:
            a = 1
        if arrayA[i] % numB == 0:
            b = 1

    if a == 1 and b == 1:
        return 0
    else:
        return max(numA, numB)

print(solution([10, 17], [5, 20]))
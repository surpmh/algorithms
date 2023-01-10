# 최대공약수와 최소공배수
import math

def solution(n, m):
    return math.gcd(n, m), (n*m) / math.gcd(n, m)

print(solution(3, 12))
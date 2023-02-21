# 다음 큰 숫자
def solution(n):
    num = n+1

    while True:
        if bin(num).count('1') == bin(n).count('1'):
            return num
        num += 1

print(solution(78))
# 자릿수 더하기
def solution(n):
    n = list(str(n))

    return sum([int(i) for i in n])

print(solution(123))
# 점프와 순간 이동
def solution(n):
    answer = 0
    
    while n > 0:
        answer += n % 2
        n //= 2

    return answer

print(solution(5))
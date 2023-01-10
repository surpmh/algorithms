# 콜라 문제
def solution(a, b, n):
    answer = 0
    
    while a <= n:
        answer += (n // a) * b
        n = ((n // a) * b) + n % a 
    
    return answer

print(solution(2, 1, 20))
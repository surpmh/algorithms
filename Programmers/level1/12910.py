# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    return [-1] if len(answer) == 0 else sorted(answer)

print(solution([5, 9, 7, 10], 5))
# 없는 숫자 더하기
def solution(numbers):
    arr = set([i for i in range(10)])
    answer = sum(arr - set(numbers))
    
    return answer

print(solution([1,2,3,4,6,7,8,0]))
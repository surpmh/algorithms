# 자연수 뒤집어 배열로 만들기
def solution(n):
    n = list(str(n))
    n.reverse()
    answer = [int(i) for i in n]
    
    return answer

print(solution(12345))
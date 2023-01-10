# 수박수박수박수박수박수?
def solution(n):
    answer = ''
    
    for i in range(n):
        answer += '수박'[i % 2]
        
    return answer

print(solution(3))
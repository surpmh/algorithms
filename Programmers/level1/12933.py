# 정수 내림차순으로 배치하기
def solution(n):
    n = list(map(int, str(n)))
    n.sort(reverse=True)
    
    answer = ''.join(map(str, n))
    
    return int(answer)

print(solution(118372))
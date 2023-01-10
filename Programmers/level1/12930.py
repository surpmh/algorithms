# 이상한 문자 만들기
def solution(s):
    count = 0
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
            count = 0
        elif count % 2 == 0:
            answer += i.upper()
            count += 1
        else:
            answer += i.lower()
            count += 1
            
    return answer

print(solution("try hello world"))
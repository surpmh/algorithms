# 문자열 내림차순으로 배치하기
def solution(s):
    s = list(s)
    answer = ''.join(reversed(sorted(s)))
    return answer

print(solution("Zbcdefg"))
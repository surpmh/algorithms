# 크기가 작은 부분문자열
def solution(t, p):
    answer = 0

    for i in range(len(t)-len(p)+1):
        part = t[i:i+len(p)]

        if int(part) <= int(p):
            answer += 1

    return answer

print(solution("10203", "15"))
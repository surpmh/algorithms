# 가장 긴 팰린드롬
def solution(s):
    answer = 0

    if len(s) == 1:
        return 1

    for i in range(len(s)-1):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))

    return answer

print(solution("abcdcba"))
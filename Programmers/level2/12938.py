# 최고의 집합
def solution(n, s):
    answer = []

    if s < n :
        return [-1]

    for _ in range(n):
        answer.append(s//n)

    idx = len(answer)-1

    for _ in range(s - sum(answer)):
        answer[idx] += 1
        idx -= 1

    return answer

print(solution(2, 9))
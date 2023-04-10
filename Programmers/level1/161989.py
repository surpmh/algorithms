# 덧칠하기
def solution(n, m, section):
    answer = 0
    l = 0

    for i in section:
        if i <= l:
            continue
        l = i + m - 1
        answer += 1

    return answer

print(solution(8, 4, [2, 3, 6]))
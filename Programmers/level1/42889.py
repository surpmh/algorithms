# 실패율
def solution(N, stages):
    answer = {}
    num = len(stages)

    for i in range(1, N+1):
        if num == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i) / num
            num -= stages.count(i)

    return sorted(answer, key=lambda x: answer[x], reverse=True)

print(solution(5, [2,2,2,2,2]))
# 과일 장수
def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    box = []

    for s in score:
        box.append(s)

        if len(box) == m:
            answer += m * box.pop()
            box = []

    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
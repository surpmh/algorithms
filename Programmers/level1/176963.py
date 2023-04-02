# 추억 점수
def solution(name, yearning, photo):
    answer = [0] * len(photo)
    dict = {}

    for n, y in zip(name, yearning):
        dict[n] = y
    # dictionary = dict(zip(name, yearning))

    for i in range(len(photo)):
        for j in photo[i]:
            if j in dict:
                answer[i] += dict[j]

    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
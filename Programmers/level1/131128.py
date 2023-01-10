# 숫자 짝꿍
def solution(X, Y):
    x = [0] * 10
    y = [0] * 10
    answer = ""

    for i in X:
        x[int(i)] += 1

    for i in Y:
        y[int(i)] += 1

    for i in range(9, -1, -1):
        n = min(x[i], y[i])
        if n:
            answer += str(i) * n

    if not answer:
        return "-1"
    elif set(answer) == {'0'}:
        return "0"
    else:
        return answer

print(solution("100", "2345"))
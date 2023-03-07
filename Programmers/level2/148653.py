# 마법의 엘리베이터
def solution(storey):
    answer = 0
    num = 0

    while storey:
        num = storey % 10

        if num > 5:
            answer += 10 - num
            storey += 10
        elif num < 5:
            answer += num
        else:
            answer += num
            if (storey // 10) % 10 >= 5:
                storey += 10

        storey //= 10

    return answer

print(solution(16))
# 카펫
def solution(brown, yellow):
    l = (brown - 4) // 2
    h = 0
    w = 0

    for i in range(1, l):
        if i * (l - i) == yellow:
            h = i
            w = l -i
            break

    answer = [w+2, h+2]

    return answer

print(solution(10, 2))
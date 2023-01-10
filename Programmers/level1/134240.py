# 푸드 파이트 대회
def solution(food):
    left = ''
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            left += str(i)

    right = left[::-1]

    return left + "0" + right

print(solution([1, 3, 4, 6]))
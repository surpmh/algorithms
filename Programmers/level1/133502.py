# 햄버거 만들기
def solution(ingredient):
    answer = 0
    stack = []

    for i in ingredient:
        stack.append(i)

        if len(stack) >= 4:
            if stack[-1:-5:-1] == [1, 3, 2, 1]:
                del stack[-1:-5:-1]
                answer += 1

    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
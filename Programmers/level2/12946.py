# 하노이의 탑
def solution(n):
    def hanoi(n, start, end, assist):
        if n == 1:
            answer.append([start, end])
            return

        hanoi(n-1, start, assist, end)
        answer.append([start, end])
        hanoi(n-1, assist, end, start)

    answer = []
    hanoi(n, 1, 3, 2)

    return answer

print(solution(2))
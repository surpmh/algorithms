# 프린터
def solution(priorities, location):
    answer = 0
    idx = 0

    while True:
        if priorities[idx] == max(priorities):
            if idx == location:
                answer += 1
                break
            else:
                answer += 1
                priorities[idx] = 0

        idx = (idx + 1) % len(priorities)

    return answer

print(solution([2, 1, 3, 2], 2))
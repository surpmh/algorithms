# 예산
def solution(d, budget):
    answer = 0
    sum = 0
    
    for amount in sorted(d):
        sum += amount
        if sum <= budget:
            answer += 1
        else:
            break

    return answer

print(solution([1,3,2,5,4], 9))
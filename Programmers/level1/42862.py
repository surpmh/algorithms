# 체육복
def solution(n, lost, reserve):
    answer = 0

    temp = set(lost) - set(reserve)
    reserve = set(reserve) - set(lost)
    lost = temp

    lost = sorted(lost)
    reserve = sorted(reserve)

    print(lost, reserve)
    
    for i in range(1, n+1):
        if i in lost:
            if i-1 in reserve:
                reserve.remove(i-1)
                answer += 1
            elif i+1 in reserve:
                reserve.remove(i+1)
                answer += 1
        else:
            answer += 1
        
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
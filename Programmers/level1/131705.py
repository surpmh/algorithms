# 삼총사
def solution(number):
    answer = 0
    length = len(number)
    
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                if not number[i] + number[j] + number[k]:
                    answer += 1
                    
    return answer
print(solution([-2, 3, 0, 2, -5]))
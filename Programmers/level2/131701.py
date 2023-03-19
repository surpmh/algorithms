# 연속 부분 수열 합의 개수
def solution(elements):
    answer = set()
    elements = elements * 2

    for i in range(1, len(elements)//2+1):
        for j in range(len(elements)//2):
            answer.add(sum(elements[j:j+i]))
        
    return len(answer)

print(solution([7,9,1,1,4]))
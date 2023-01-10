# 성격 유형 검사하기
def solution(survey, choices):
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            dict[survey[i][0]] += (4 - choices[i])
        elif choices[i] > 4:
            dict[survey[i][1]] += (choices[i] - 4)

    answer = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']

    for i in range(4):
        if dict[answer[i]] < dict[answer[i+1]]:
            answer.remove(answer[i])
        else:
            answer.remove(answer[i+1])
            
    answer = ''.join(s for s in answer)
        
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# 인사고과
def solution(scores):
    answer = 1
    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key = lambda x : (-x[0], x[1]))
    temp = 0
    
    for score in scores:
        if score[0] > target[0] and score[1] > target[1]:
            return -1
        
        if temp <= score[1]:
            if target_score < sum(score):
                answer += 1
            temp = score[1]

    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
# 신고 결과 받기
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    result = [0 for _ in range(len(id_list))]
    
    report = set(report)
    report = list(report)
    
    for i in range(len(report)):
        a, b = report[i].split()

        answer[id_list.index(b)] += 1
        
    for i in range(len(answer)):
        if answer[i] < k:
            answer[i] = 0

    for i in range(len(report)):
        a, b = report[i].split()
        
        if answer[id_list.index(b)] >= k:
            result[id_list.index(a)] += 1

    return result

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
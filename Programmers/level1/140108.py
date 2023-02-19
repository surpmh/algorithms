# 문자열 나누기
def solution(s):
    answer = 0
    arr = []

    for i in s:
        arr.append(i)

        if len(arr) > 1 and arr.count(arr[0]) == len(arr) - arr.count(arr[0]):
            arr = []
            answer += 1
        
    if arr:
        answer += 1
    
    return answer

print(solution("banana"))
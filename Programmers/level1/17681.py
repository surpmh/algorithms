# [1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        answer.append(bin(i | j)[2:].zfill(n).replace("1", "#").replace("0", " "))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
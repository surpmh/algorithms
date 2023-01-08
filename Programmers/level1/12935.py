# 제일 작은 수 제거하기
def solution(arr):
    if 2 < len(arr):
        arr.remove(min(arr))
    else:
        arr = [-1]
        
    return arr

print(solution([4,3,2,1]))
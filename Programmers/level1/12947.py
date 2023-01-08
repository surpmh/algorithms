# 하샤드 수
def solution(x):
    x = str(x)
    sum = 0

    for i in range(len(x)):
        s = int(x[i])
        sum += s
    
    x = int(x)
    if x % sum == 0:
        answer = True
    else:
        answer = False
        
    return answer

print(solution(10))
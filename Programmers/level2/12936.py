# 줄 서는 방법
import math

def solution(n, k):
    answer = []
    k -= 1
    arr = [i for i in range(1, n+1)]
    
    for i in range(n-1, -1, -1):
        if k == 0:
            answer += arr
            break

        idx = int(k / math.factorial(i))
        answer.append(arr.pop(idx))
        k = k % math.factorial(i)

    return answer

print(solution(3, 5))
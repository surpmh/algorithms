# 약수의 개수와 덧셈
import math

def divisor(n):
    count = 0
    
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            count += 1
            if n //i != i:
                count += 1
                
    return count

def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        if divisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

print(solution(13, 17))
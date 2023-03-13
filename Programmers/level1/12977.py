# 소수 만들기
import math
from itertools import combinations

def solution(nums):
    answer = 0
    prime = [True] * 3001

    for i in range(2, int(math.sqrt(3000))+1):
        if prime[i] == True:
            for j in range(i*2, 3001, i):
                prime[j] = False
    
    prime[0], prime[1] = False, False

    for i in list(combinations(nums, 3)):
        if prime[sum(i)]:
            answer += 1
    
    return answer

print(solution([1,2,3,4]))
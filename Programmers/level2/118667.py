# 두 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    answer = 0

    if (sum1 + sum2) % 2 == 1:
        return -1
    
    for i in range((sum1 + sum2)):
        if i == 600000:
            break
        if sum1 < sum2:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
        elif sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        else:
            return answer
        answer += 1
        
    return -1

print(solution([1, 2, 4], [3, 2, 4]))
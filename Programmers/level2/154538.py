# 숫자 변환하기
from collections import deque

def solution(x, y, n):
    q = deque()
    q.append(x)
    count = [0] * (y+1)

    if x==y: return 0

    while q:
        x = q.popleft()
        
        for i in (x + n, x * 2, x * 3):
            if i == y:
                return count[x] + 1
            
            if 0 < i < y and not count[i]:
                count[i] = count[x] + 1
                q.append(i)

    return -1

print(solution(10, 40, 5))
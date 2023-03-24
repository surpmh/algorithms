# 네트워크
from collections import deque

def bfs(computers, visited, n):
    q = deque()
    q.append(n)
    visited[n] = True

    while q:
        v = q.popleft()
        
        for i in range(len(computers[v])):
            if computers[v][i] and not visited[i]:
                q.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
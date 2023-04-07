# 스킬트리
from collections import deque

def solution(skill, skill_trees):
    answer = len(skill_trees)

    for s in skill_trees:
        q = deque(skill)
        for i in s:
            if i in q:
                if i == q[0]:
                    q.popleft()
                else:
                    answer -= 1
                    break

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
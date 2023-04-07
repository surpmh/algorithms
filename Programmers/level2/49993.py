# 스킬트리
def solution(skill, skill_trees):
    answer = len(skill_trees)

    for s in skill_trees:
        learn = [0] * len(skill)
        for i in s:
            if i in skill:
                if i == skill[0]:
                    learn[0] = 1
                elif learn[skill.find(i)-1]:
                    learn[skill.find(i)] = 1
                else:
                    answer -= 1
                    break

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
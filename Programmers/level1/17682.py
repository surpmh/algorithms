# [1차] 다트 게임
def solution(dartResult):
    stack = []
    n = ""

    for s in dartResult:
        if s == "S":
            stack.append(int(n)**1)
            n = ""
        elif s == "D":
            stack.append(int(n)**2)
            n = ""
        elif s == "T":
            stack.append(int(n)**3)
            n = ""
        elif s == "*":
            n = stack.pop()
            if stack:
                stack.append(stack.pop()*2)
            stack.append(int(n)*2)
            n = ""
        elif s == "#":
            stack.append(stack.pop()*-1)
            n = ""
        else:
            n += s

    return sum(stack)

print(solution("1S2D*3T"))
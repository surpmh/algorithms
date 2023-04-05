# 큰 수 만들기
def solution(number, k):
    stack = []

    for n in number:
        while stack and n > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)

print(solution("99991", 3))
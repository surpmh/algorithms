# 둘만의 암호
def solution(s, skip, index):
    answer = ''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        alphabet.remove(i)

    for i in s:
        answer += alphabet[(alphabet.index(i) + index) % len(alphabet)]

    return answer

print(solution("aukks", "wbqd", 5))
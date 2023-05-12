# [3차] 압축
def solution(msg):
    dict = {chr(i+64) : i for i in range(1, 27)}
    answer = []
    idx = 27

    while msg:
        for i in range(len(msg), -1, -1):
            if msg[:i+1] in dict:
                answer.append(dict[msg[:i+1]])
                dict[msg[:i+2]] = idx
                msg = msg[i+1:]
                idx += 1
                break

    return answer

print(solution("KAKAO"))
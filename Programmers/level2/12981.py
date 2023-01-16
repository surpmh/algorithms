# 영어 끝말잇기
def solution(n, words):
    answer = [0, 0]
    last = words[0][-1]

    for i in range(1, len(words)):
        if words[i] in words[:i] or words[i][0] is not last:
            answer = [i%n+1, i//n+1]
            break
            
        last = words[i][-1]

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
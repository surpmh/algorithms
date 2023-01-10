# 완주하지 못한 선수
def solution(participant, completion):
    answer = ""
    player = {}

    for p in participant:
        if p not in player:
            player[p] = 1
        else:
            player[p] += 1

    for c in completion:
        player[c] -= 1

    for p in player:
        if player[p] != 0:
            answer = p

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
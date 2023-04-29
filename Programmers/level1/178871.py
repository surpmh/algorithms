# 달리기 경주
def solution(players, callings):
    p = {}
    r = {}

    for i in range(len(players)):
        p[players[i]] = i + 1
        r[i + 1] = players[i]

    for call in callings:
        rank = p[call]
        player = r[rank - 1]

        p[call] -= 1
        r[rank - 1] = call
        r[rank]  = player
        p[player] += 1

    return list(r.values())

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
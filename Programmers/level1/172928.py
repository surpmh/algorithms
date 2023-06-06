# 공원 산책
def solution(park, routes):
    idx = [0, 0]
    move = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                idx = [i, j]

    for route in routes:
        dir, dis = route.split(" ")
        temp = [0, 0]
        temp[0] = idx[0]
        temp[1] = idx[1]
        for _ in range(int(dis)):
            idx[0] += move[dir][0]
            idx[1] += move[dir][1]

            if idx[0] < 0 or idx[0] >= len(park) or idx[1] < 0 or idx[1] >= len(park[0]) or park[idx[0]][idx[1]] == "X":
                idx = temp
                break
            
    return idx

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
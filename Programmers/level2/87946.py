# 피로도
answer = 0

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)

    dfs(k, 0, dungeons, visited)

    return answer

def dfs(k, count, dungeons, viseited):
    global answer
    if count > answer:
        answer = count

    for i in range(len(dungeons)):
        if not viseited[i] and dungeons[i][0] <= k:
            viseited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons, viseited)
            viseited[i] = False

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
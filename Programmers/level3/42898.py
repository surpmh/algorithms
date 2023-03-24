# 등굣길
def solution(m, n, puddles):
    maps = [[0] * m for _ in range(n)]

    for i in range(m):
        if [i+1, 1] in puddles:
            break
        maps[0][i] = 1

    for i in range(n):
        if [1, i+1] in puddles:
            break
        maps[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            maps[i][j] = (maps[i][j-1] + maps[i-1][j]) % 1000000007

            if [j+1, i+1] in puddles:
                maps[i][j] = 0
                
    return maps[n-1][m-1]

print(solution(4, 3, [[2, 2]]))
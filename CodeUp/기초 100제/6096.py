# [기초-리스트] 바둑알 십자 뒤집기
board = [list(map(int, input().split())) for _ in range(19)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(19):
        if board[x-1][i] == 0:
            board[x-1][i] = 1
        else:
            board[x-1][i] = 0
        if board[i][y-1] == 0:
            board[i][y-1] = 1
        else:
            board[i][y-1] = 0

for r in board:
    print(*r)
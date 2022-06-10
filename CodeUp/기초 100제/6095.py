# [기초-리스트] 바둑판에 흰 돌 놓기
board = [[0 for i in range(19)] for j in range(19)]

n = int(input())

for _ in range(n):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

for result in board:
    print(*result)
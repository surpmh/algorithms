# [기초-리스트] 설탕과자 뽑기
h, w = map(int, input().split())
n = int(input())

board = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(n):
    l, d, y, x = map(int, input().split())

    if d == 0:
        for i in range(l):
            board[y-1][x-1+i] = 1
    else:
        for i in range(l):
            board[y-1+i][x-1] = 1

for i in board:
    print(*i)
# 스도쿠
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
blank = [[i, j] for i in range(9) for j in range(9) if board[i][j] == 0]

def check(y, x):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if board[i][x] in num:
            num.remove(board[i][x])

        if board[y][i] in num:
            num.remove(board[y][i])

    y //= 3
    x //= 3
    for i in range(y*3, (y+1)*3):
        for j in range(x*3, (x+1)*3):
            if board[i][j] in num:
                num.remove(board[i][j])

    return num

solve = False

def sudoku(count):
    global solve
    
    if solve:
        return

    if count == len(blank):
        for row in board:
            print(*row)
        solve = True
        return
    
    i, j = blank[count]
    num = check(i, j)
    for n in num:
        board[i][j] = n
        sudoku(count + 1)
        board[i][j] = 0

sudoku(0)
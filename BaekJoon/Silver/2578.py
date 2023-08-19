# 빙고
import sys
input = sys.stdin.readline

def check_bingo(board):
    bingo = 0

    for line in board: 
        if sum(line) == 0:
            bingo += 1

    for i in range(5): 
        check = 0
        for j in range(5):
            check += board[j][i]

        if check == 0:
            bingo += 1

    check = 0
    for i in range(5):
        check += board[i][i]
    
    if check == 0:
            bingo += 1

    check = 0
    for i in range(5):
        check += board[i][4-i]
    
    if check == 0:
            bingo += 1

    return bingo

board = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

for order in range(len(nums)):
    for i in range(5):
        for j in range(5):
            if board[i][j] == nums[order]:
                board[i][j] = 0

            if order > 10:
                if check_bingo(board) >= 3:
                    print(order+1)
                    exit()

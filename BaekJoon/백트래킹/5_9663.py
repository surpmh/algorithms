# N-Queen
import sys
input = sys.stdin.readline

n = int(input())
board = [0] * n
result = 0

def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            board[x] = i
            if check(x):
                dfs(x+1)

dfs(0)
print(result)
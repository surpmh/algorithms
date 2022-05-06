# 체스판 다시 칠하기
import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    board = []

    for i in range(m):    
        board.append(list(map(str, sys.stdin.readline().rstrip())))

    for i in range(n-7):
        for j in range(m-7):
            if board[i][j]

if __name__ == "__main__":
    main()
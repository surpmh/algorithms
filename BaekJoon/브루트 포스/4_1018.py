# 체스판 다시 칠하기
def main():
    m, n = map(int, input().split())
    board = []
    count = []

    for i in range(m):
        board.append(input())

    for i in range(m-7):
        for j in range(n-7):
            index1 = 0
            index2 = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if (k+l) % 2 == 0:
                        if board[k][l] != 'W':
                            index1 += 1
                        if board[k][l] != 'B':
                            index2 += 1
                    else:
                        if board[k][l] != 'B':
                            index1 += 1
                        if board[k][l] != 'W':
                            index2 += 1
            count.append(min(index1, index2))
    
    print(min(count))         

if __name__ == "__main__":
    main()
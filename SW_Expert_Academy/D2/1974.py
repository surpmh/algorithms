# 스도쿠 검증
def check(board):
    for i in range(9):
        check = []
        for j in range(9):
            if check:
                if board[i][j] in check:
                    return '0'
            check.append(board[i][j])
    
    for i in range(9):
        check = []
        for j in range(9):
            if check:
                if board[j][i] in check:
                    return '0'
            check.append(board[j][i])
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []
            for k in range(3):
                for l in range(3):
                    if check:
                        if board[i+k][j+l] in check:
                            return '0'
                    check.append(board[i+k][j+l])

    return '1'

def main():
    T = int(input())

    for test_case in range(1, T + 1):
        board = [list(map(int, input().split())) for _ in range(9)]

        print("#{0}".format(test_case), check(board))
            
if __name__ == "__main__":
    main()
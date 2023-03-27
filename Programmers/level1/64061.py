# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack = [0]
    
    for move in moves:
        for row in board:
            if row[move-1]:
                num = row[move-1]
                row[move-1] = 0
                if stack[-1] == num:
                    stack.pop()
                    answer += 2
                    break
                else:
                    stack.append(num)
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
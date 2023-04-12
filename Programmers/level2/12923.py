# 숫자 블록
def solution(begin, end):
    answer = []

    for i in range(begin, end+1):
        num = 0
        if i == 1:
            answer.append(0)
        else:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    if i // j <= 10000000:
                        answer.append(i // j)
                    else:
                        num = j
                        continue
                    break
            else:
                if num:
                    answer.append(num)
                else:
                    answer.append(1)

    return answer

print(solution(100000014, 100000016))
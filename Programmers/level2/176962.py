# 과제 진행하기
from collections import deque

def solution(plans):
    answer = []
    plans.sort(key=lambda x:x[1])
    homework = []

    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        end = h*60+m+int(plans[i][2])

        if i+1 < len(plans):
            h, m = map(int, plans[i+1][1].split(":"))
            start = h*60+m

            if end < start:
                spare = start - end
                answer.append(plans[i][0])
                while homework:
                    print(homework[-1][1])
                    if spare >= homework[-1][1]:
                        answer.append(homework.pop()[0])
                    else:
                        homework[-1][1] -= spare
                        break
            elif end > start:
                homework.append([plans[i][0], end-start])
            else:
                answer.append(plans[i][0])
        else:
            answer.append(plans[i][0])

    while homework:
        answer.append(homework.pop()[0])

    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    cnt = lottos.count(0)
    if cnt == 6:
        cnt -= 1

    if len(set(lottos) & set(win_nums)) < 2:
        result = 6
    else:
        result = 7 - len(set(lottos) & set(win_nums))

    answer= [result-cnt, result]
    
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
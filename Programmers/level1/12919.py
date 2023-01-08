# 서울에서 김서방 찾기
def solution(seoul):
    answer = seoul.index("Kim")
    return '김서방은 {0}에 있다'.format(answer)

print(solution(["Jane", "Kim"]))
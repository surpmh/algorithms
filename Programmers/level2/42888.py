# 오픈채팅방
def solution(record):
    answer = []
    dict = {}

    for i in record:
        info = i.split()
        if info[0] != "Leave":
            dict[info[1]] = info[2]

    for i in record:
        info = i.split()
        if info[0] == "Enter":
            answer.append(dict[info[1]] + "님이 들어왔습니다.")
        elif info[0] == "Leave":
            answer.append(dict[info[1]] + "님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
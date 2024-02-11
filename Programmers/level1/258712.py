# 가장 많이 받은 선물
def solution(friends, gifts):
    friend_num = len(friends)
    arr = [[0] * friend_num for _ in range(friend_num)]
    gift_dict = dict.fromkeys(friends, 0)
    answer = dict.fromkeys(friends, 0)
    friend_idx = {name: index for index, name in enumerate(friends)}

    for gift in gifts:
        a, b = gift.split()
        arr[friend_idx[a]][friend_idx[b]] += 1
        gift_dict[a] += 1
        gift_dict[b] -= 1

    for i in range(friend_num):
        for j in range(i+1, friend_num):
            if arr[i][j] > arr[j][i]:
                answer[friends[i]] += 1
            elif arr[i][j] < arr[j][i]:
                answer[friends[j]] += 1
            else:
                if gift_dict[friends[i]] > gift_dict[friends[j]]:
                    answer[friends[i]] += 1
                elif gift_dict[friends[i]] < gift_dict[friends[j]]:
                    answer[friends[j]] += 1

    return max(answer.values())

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
# 할인 행사
def solution(want, number, discount):
    answer = 0

    for i in range(len(discount)-9):
        list = discount[i:i+10]
        for j in range(len(want)):
            if list.count(want[j]) < number[j]:
                break
            if j == len(want)-1:
                answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
# 옹알이
def solution(babbling):
    pronunciation = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        say = ""
        before = ""
        for alphabet in word:
            say += alphabet

            if say == before:
                continue

            if say in pronunciation:
                before = say
                say = ""

        if say == "":
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))
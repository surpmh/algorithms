# 숫자 문자열과 영단어
def solution(s):
    dict = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    for key in dict.keys():
        if key in s:
            s = s.replace(key, dict[key])

    return int(s)

print(solution("one4seveneight"))
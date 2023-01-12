# JadenCase 문자열 만들기
def solution(s):
    words = s.lower()
    words = words[0].upper() + words[1:]

    for i in range(1, len(words)):
        if words[i-1] == " ":
            words = words[:i] + words[i].upper() + words[i+1:]
    
    return words

print(solution("3people unFollowed me"))
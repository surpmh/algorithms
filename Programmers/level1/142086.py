# 가장 가까운 같은 글자
def solution(s):
    answer = []
    dict = {}
    
    for i in range(len(s)):
        if s[i] in dict.keys():
            answer.append(i - dict[s[i]])
            dict[s[i]] = i
        else:
            answer.append(-1)
            dict[s[i]] = i
        
    return answer

print(solution("banana"))
# 시저 암호
def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
            continue
            
        c = ord(i) + n
        if 65 <= ord(i) <= 90:
            if c > 90:
                c -= 26
        else:
            if c > 122:
                c -= 26
                
        answer += chr(c)
        
    return answer

print(solution("AB", 1))
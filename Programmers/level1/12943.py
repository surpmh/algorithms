# 콜라츠 추측
def solution(num):
    count = 0
    
    while True:
        if num == 1:
            return count
        elif count == 500:
            return -1
        
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1

print(solution(6))
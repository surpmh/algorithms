# 기사단원의 무기
def count_divisor(n):
    divisor = []

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisor.append(i)
            if (i**2) != n:
                divisor.append(n // i)

    return len(divisor)

def solution(number, limit, power):
    answer = 0

    for i in range(1, number+1):
        weight = count_divisor(i)

        if weight <= limit:
            answer += weight
        else:
            answer += power

    return answer

print(solution(5, 3, 2))
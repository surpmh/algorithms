# N개의 최소공배수
def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def solution(arr):
    answer = arr[0]

    for num in arr:
        answer = answer * num // gcd(answer, num)

    return answer

print(solution([2,6,8,14]))
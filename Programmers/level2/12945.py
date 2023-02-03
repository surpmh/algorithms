# 피보나치 수
def solution(n):
    dp = [0] * 100001
    dp[0] = 0
    dp[1] = 1

    if n < 2:
        return n

    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1] % 1234567

    return dp[n]

print(solution(3))
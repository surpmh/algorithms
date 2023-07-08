# 스티커 모으기(2)
def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)
    
    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)
    dp1[0], dp1[1] = sticker[0], sticker[0]

    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])

    for i in range(1, len(sticker)):
        dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-1])

    return max(dp1[-2], dp2[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
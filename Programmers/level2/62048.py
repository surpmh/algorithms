# 멀쩡한 사각형
def gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a

def solution(w, h):
    if w < h:
        w, h = h, w

    return w * h - (w + h - gcd(w, h))

print(solution(8, 12))
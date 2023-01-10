# 최소직사각형
def solution(sizes):
    h = []
    w = []
    for i, j in sizes:
        if i < j:
            h.append(i)
            w.append(j)
        else:
            w.append(i)
            h.append(j)
            
    answer = max(h) * max(w)
            
    return answer
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))